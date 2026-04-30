import os
import time
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai
import re

# -------------------------------
# LOAD ENV VARIABLES
# -------------------------------
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not found")

genai.configure(api_key=api_key)

# -------------------------------
# CONFIG
# -------------------------------
MODEL = os.getenv("MODEL", "gemini-2.5-flash")
TEMPERATURE = 0
MAX_TOKENS = 1024  # safe limit to avoid duplication or truncation

# 🔒 SAFE RPM (under 5)
REQUESTS_PER_MINUTE = 2
DELAY = 240 / REQUESTS_PER_MINUTE  # 60 sec between requests

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

PROMPT_TYPES = ["zero_shot", "few_shot", "structured", "cot"]
RUNS_PER_PROMPT = 1

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
    """Remove markdown code fences and extra 'python' labels."""
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


def remove_duplicate_functions(code: str, function_name: str) -> str:
    """Keep only the last occurrence of the function definition if repeated."""
    pattern = rf"(def {function_name}\(.*?\):.*?)(?=def {function_name}\(|\Z)"
    matches = re.findall(pattern, code, flags=re.DOTALL)
    return matches[-1] if matches else code


def generate_test(function_code: str, prompt_template: str, func_name: str) -> str:
    """Generate one valid test code for the function using Gemini."""
    prompt = prompt_template.replace("<function_code_here>", function_code)
    model = genai.GenerativeModel(MODEL)

    for attempt in range(5):
        try:
            response = model.generate_content(
                prompt,
                generation_config={
                    "temperature": TEMPERATURE,
                    "max_output_tokens": MAX_TOKENS,
                    "top_p": 1,
                }
            )

            text = getattr(response, "text", "")
            text = clean_code_output(text)

            # Remove duplicate function definitions if they exist
            text = remove_duplicate_functions(text, func_name)

            if text and is_valid_python(text):
                return text

            print("⚠ Invalid output, retrying...")

        except Exception as e:
            wait = 2 ** attempt + 1
            print(f"⚠ Error: {e} | retrying in {wait}s")
            time.sleep(wait)

    return ""


def save_code(code: str, path: Path, function_code: str):
    """Save the full test file including function code and generated tests."""
    path.parent.mkdir(parents=True, exist_ok=True)
    full_code = function_code + "\n\n" + code
    path.write_text(full_code, encoding="utf-8")


# -------------------------------
# MAIN
# -------------------------------
def main():
    print("🚀 Generating tests (RPM-safe mode)")
    print(f"⏱ Delay between requests: {DELAY:.1f}s\n")

    for func_file in FUNCTIONS_FOLDER.glob("*.py"):
        print(f"📄 Processing function: {func_file.name}")
        function_code = func_file.read_text(encoding="utf-8")

        # Extract function name
        func_match = re.search(r"def (\w+)\(", function_code)
        if not func_match:
            print("⚠ Could not detect function name, skipping...")
            continue
        func_name = func_match.group(1)

        for prompt_type in PROMPT_TYPES:
            print(f"   🔹 Prompt type: {prompt_type}")
            prompt_template = load_prompt(prompt_type)
            if not prompt_template.strip():
                continue

            test_code = generate_test(function_code, prompt_template, func_name)
            if not test_code:
                print("   ❌ Generation failed, skipping")
                continue

            out_file = OUTPUT_FOLDER / prompt_type / f"{func_file.stem}.py"
            save_code(test_code, out_file, function_code)
            print(f"   ✅ Saved: {out_file}")

            print(f"   ⏳ Waiting {DELAY:.1f}s to respect RPM...")
            time.sleep(DELAY)

    print("\n🎉 All tests generated successfully!")


if __name__ == "__main__":
    main()