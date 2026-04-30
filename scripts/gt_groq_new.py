import os
import time
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
import re

# -------------------------------
# LOAD ENV VARIABLES
# -------------------------------
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("❌ GROQ_API_KEY not found")

client = Groq(api_key=api_key)

# -------------------------------
# CONFIG
# -------------------------------
MODEL = os.getenv("MODEL", "moonshotai/kimi-k2-instruct-0905")
MODEL_NAME = MODEL.replace("/", "-")

TEMPERATURE = 0.4
# FIX [1]: Increased from 1024 → 2048 to prevent truncation of test suites,
# especially for few-shot prompts which consume more input tokens.
MAX_TOKENS = 2048

REQUESTS_PER_MINUTE = 2
DELAY = 60 / REQUESTS_PER_MINUTE

# Methodology: each function-prompt pair is run 3 times and results averaged.
RUNS_PER_PROMPT = 3

# -------------------------------
# PATHS
# -------------------------------
try:
    BASE_DIR = Path(__file__).resolve().parent.parent
except NameError:
    BASE_DIR = Path.cwd()

FUNCTIONS_FOLDER = BASE_DIR / "functions"
PROMPTS_FOLDER = BASE_DIR / "prompts"
OUTPUT_FOLDER = BASE_DIR / "generated_tests"
MUTATION_FOLDER = BASE_DIR / "mutants"

PROMPT_TYPES = ["zero_shot", "few_shot", "structured", "cot"]

# -------------------------------
# HELPERS
# -------------------------------
def load_prompt(prompt_type: str) -> str:
    path = PROMPTS_FOLDER / f"{prompt_type}.txt"
    if not path.exists():
        print(f"⚠ Missing prompt: {path}")
        return ""
    return path.read_text(encoding="utf-8")


def clean_code_output(text: str) -> str:
    text = text.strip()
    if text.startswith("```"):
        lines = text.split("\n")
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        if lines and lines[0].startswith("python"):
            lines = lines[1:]
        text = "\n".join(lines)
    return text


def is_valid_python(code: str) -> bool:
    try:
        compile(code, "<string>", "exec")
        return True
    except SyntaxError:
        return False


def strip_function_definitions(code: str, func_name: str) -> str:
    """
    Removes ANY re-definition of the target function from generated output.
    Ensures test file NEVER embeds the original function (import is injected
    at eval time by the evaluator).
    """
    pattern = rf"def {func_name}\(.*?\):.*?(?=\ndef |\Z)"
    return re.sub(pattern, "", code, flags=re.DOTALL)


# -------------------------------
# TEST GENERATION
# -------------------------------
def generate_test(function_code: str, prompt_template: str, func_name: str) -> str:
    prompt = prompt_template.replace("<function_code_here>", function_code)

    for attempt in range(5):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": prompt}],
                temperature=TEMPERATURE,
                max_tokens=MAX_TOKENS,
                top_p=1,
            )

            text = response.choices[0].message.content or ""
            text = clean_code_output(text)
            text = strip_function_definitions(text, func_name)

            if text and is_valid_python(text):
                return text

            print("⚠ Invalid output, retrying...")

        except Exception as e:
            wait = 2 ** attempt + 1
            print(f"⚠ Error: {e} | retrying in {wait}s")
            time.sleep(wait)

    return ""


def save_test(code: str, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(code, encoding="utf-8")


# -------------------------------
# MUTATION GENERATION
# -------------------------------
def generate_mutant(function_code: str) -> str:
    """
    Generate ONE mutated version of the function using the LLM.
    Methodology: mutation score measures ability of tests to detect
    artificially introduced faults.
    """
    mutation_prompt = f"""
You are performing mutation testing.

Given this Python function, create ONE mutated version of it by introducing a small logical fault.
Examples of mutations:
- Change comparison operators (>, <, ==)
- Modify arithmetic (+ to -, etc.)
- Off-by-one errors
- Incorrect condition

Return ONLY the mutated function code, no explanation, no markdown.

Function:
{function_code}
"""

    for attempt in range(5):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": mutation_prompt}],
                temperature=0,
                max_tokens=512,
            )

            text = response.choices[0].message.content or ""
            text = clean_code_output(text)

            if text and is_valid_python(text):
                return text

        except Exception as e:
            wait = 2 ** attempt + 1
            print(f"⚠ Mutation error: {e} | retrying in {wait}s")
            time.sleep(wait)

    return ""


def save_mutant(code: str, func_name: str):
    """Save ONE mutant per function (generated once, reused across all prompt strategies)."""
    MUTATION_FOLDER.mkdir(parents=True, exist_ok=True)
    path = MUTATION_FOLDER / f"{func_name}_mutant.py"
    path.write_text(code, encoding="utf-8")


# -------------------------------
# RESUME HELPERS
# -------------------------------
def get_pending_runs(func_stem: str) -> dict[str, list[int]]:
    """
    For a given function file stem (e.g. 'letter_combination_of_phone_numbers'),
    check which prompt_type × run_number combinations have NOT been generated yet.
    Returns: { prompt_type: [missing_run_numbers] }
    Only runs that are completely absent are included — existing files are skipped.
    """
    pending = {}
    for prompt_type in PROMPT_TYPES:
        missing_runs = []
        for run in range(1, RUNS_PER_PROMPT + 1):
            out_file = (
                OUTPUT_FOLDER
                / MODEL_NAME
                / prompt_type
                / f"{func_stem}_run{run}.py"
            )
            if not out_file.exists():
                missing_runs.append(run)
        if missing_runs:
            pending[prompt_type] = missing_runs
    return pending


def summarise_progress() -> None:
    """Print a progress table at startup so you know exactly where to resume."""
    print("\n📋 Progress check:")
    print(f"   {'Function':<45} {'Mutant':<8} " + "  ".join(f"{p[:3]}" for p in PROMPT_TYPES))
    print(f"   {'-'*45} {'-'*8} " + "  ".join("---" for _ in PROMPT_TYPES))
    for func_file in sorted(FUNCTIONS_FOLDER.glob("*.py")):
        if func_file.name == "__init__.py":
            continue
        code = func_file.read_text(encoding="utf-8")
        m = re.search(r"def (\w+)\(", code)
        func_name = m.group(1) if m else "?"
        mutant_exists = (MUTATION_FOLDER / f"{func_name}_mutant.py").exists()
        counts = []
        for pt in PROMPT_TYPES:
            found = sum(
                1 for run in range(1, RUNS_PER_PROMPT + 1)
                if (OUTPUT_FOLDER / MODEL_NAME / pt / f"{func_file.stem}_run{run}.py").exists()
            )
            counts.append(f"{found}/{RUNS_PER_PROMPT}")
        mutant_str = "✅" if mutant_exists else "❌"
        print(f"   {func_file.stem:<45} {mutant_str:<8} " + "  ".join(f"{c:>3}" for c in counts))
    print()


# -------------------------------
# MAIN
# -------------------------------
def main():
    print(f"🚀 Generating tests for model: {MODEL_NAME}")
    print(f"   Temperature: {TEMPERATURE} | Max tokens: {MAX_TOKENS}")
    print(f"   Runs per prompt: {RUNS_PER_PROMPT} | Delay: {DELAY:.1f}s")

    summarise_progress()

    total_generated = 0
    total_skipped = 0

    for func_file in sorted(FUNCTIONS_FOLDER.glob("*.py")):
        if func_file.name == "__init__.py":
            continue

        function_code = func_file.read_text(encoding="utf-8")
        func_match = re.search(r"def (\w+)\(", function_code)
        if not func_match:
            print(f"⚠ No function def found in {func_file.name}, skipping")
            continue
        func_name = func_match.group(1)

        # Check how much work is left for this function
        pending = get_pending_runs(func_file.stem)
        total_pending = sum(len(v) for v in pending.values())

        if total_pending == 0:
            print(f"✅ {func_file.stem} — fully generated, skipping")
            total_skipped += 1
            continue

        print(f"\n📄 {func_file.stem}  (func: {func_name})")
        print(f"   Pending: { {k: v for k, v in pending.items()} }")

        # Mutant — generate only if missing
        mutant_path = MUTATION_FOLDER / f"{func_name}_mutant.py"
        if mutant_path.exists():
            print("   🧬 Mutant already exists")
        else:
            mutant_code = generate_mutant(function_code)
            if mutant_code:
                save_mutant(mutant_code, func_name)
                print("   🧬 Mutant generated")
            else:
                print("   ⚠ Mutant generation failed")

        # Generate only the missing prompt × run combinations
        for prompt_type, missing_runs in pending.items():
            print(f"   🔹 Prompt: {prompt_type}  (runs needed: {missing_runs})")
            prompt_template = load_prompt(prompt_type)
            if not prompt_template.strip():
                continue

            for run in missing_runs:
                print(f"      🔁 Run {run}/{RUNS_PER_PROMPT}")

                test_code = generate_test(function_code, prompt_template, func_name)
                if not test_code:
                    print("      ❌ Generation failed")
                    continue

                out_file = (
                    OUTPUT_FOLDER
                    / MODEL_NAME
                    / prompt_type
                    / f"{func_file.stem}_run{run}.py"
                )

                save_test(test_code, out_file)
                print(f"      ✅ Saved → {out_file.name}")
                total_generated += 1

                time.sleep(DELAY)

    print(f"\n🎉 Session complete!")
    print(f"   Generated : {total_generated} new test files")
    print(f"   Skipped   : {total_skipped} fully-done functions")
    print(f"   Output    : {OUTPUT_FOLDER / MODEL_NAME}")
    print()
    summarise_progress()


if __name__ == "__main__":
    main()