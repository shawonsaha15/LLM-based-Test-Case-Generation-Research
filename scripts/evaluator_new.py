import subprocess
import json
import os
import ast
from pathlib import Path
from collections import defaultdict

OUTPUT_FOLDER = Path(r"D:\Research\SQA\generated_tests")
FUNCTIONS_FOLDER = Path(r"D:\Research\SQA\functions")
MUTANTS_FOLDER = Path(r"D:\Research\SQA\mutants")

CWD = FUNCTIONS_FOLDER.parent          # D:\\Research\\SQA
RESULTS_FILE   = CWD / "results.json"
TEMP_TEST_FILE = CWD / "temp_test.py"
COVERAGE_FILE  = CWD / "coverage.json"


# -------------------------------
# CORE RUNNER
# -------------------------------
def run_pytest(test_file: Path, file_stem: str):
    try:
        env = os.environ.copy()
        env["PYTHONPATH"] = str(FUNCTIONS_FOLDER.parent)

        # BUG FIX 1: Scope --cov to the specific function file only.
        # Previously --cov=functions measured ALL files in functions/, so a
        # function with 100% coverage was diluted to ~12% by 10 untested files.
        # BUG FIX 2: Removed --maxfail=1. With maxfail=1, a single wrong
        # assertion aborts the whole suite and marks passed=False even if
        # 11 of 12 tests pass. Full execution is needed for honest metrics.
        cov_source = f"functions.{file_stem}"

        # Delete stale coverage.json before each run to prevent cache reads
        if COVERAGE_FILE.exists():
            COVERAGE_FILE.unlink()

        result = subprocess.run(
            [
                "pytest",
                str(test_file),
                "--disable-warnings",
                "-q",
                f"--cov={cov_source}",
                "--cov-branch",
                "--cov-report=json:coverage.json"
            ],
            capture_output=True,
            text=True,
            timeout=60,
            env=env,
            cwd=FUNCTIONS_FOLDER.parent
        )

        # returncode: 0=all passed, 1=some failed, 2=collection/import error
        executable = result.returncode != 2
        passed = result.returncode == 0

        line_coverage = 0
        branch_coverage = 0
        cov_file = COVERAGE_FILE

        if cov_file.exists():
            try:
                cov_data = json.loads(cov_file.read_text())

                # BUG FIX 3: Read per-file coverage for this function only,
                # not totals. coverage.json["files"] has one entry per source file.
                # Normalise backslashes so Windows paths match too.
                files = cov_data.get("files", {})
                per_file = None
                for key, val in files.items():
                    if key.replace("\\", "/").endswith(f"functions/{file_stem}.py"):
                        per_file = val
                        break

                if per_file:
                    summary = per_file.get("summary", {})
                    line_coverage = round(summary.get("percent_covered", 0), 2)
                    covered_b = summary.get("covered_branches", 0) or 0
                    total_b = summary.get("num_branches", 0) or 0
                    if total_b > 0:
                        branch_coverage = round((covered_b / total_b) * 100, 2)
                else:
                    # Fallback to totals if per-file lookup fails
                    totals = cov_data.get("totals", {})
                    line_coverage = round(totals.get("percent_covered", 0), 2)
                    covered_b = totals.get("covered_branches", 0) or 0
                    total_b = totals.get("num_branches", 0) or 0
                    if total_b > 0:
                        branch_coverage = round((covered_b / total_b) * 100, 2)

            except Exception:
                line_coverage = 0
                branch_coverage = 0

        return executable, passed, line_coverage, branch_coverage, result.stdout + result.stderr

    except Exception as e:
        return False, False, 0, 0, str(e)


# -------------------------------
# PREPARE TEST WITH IMPORT
# -------------------------------
def sanitize_test_code(test_code: str, function_name: str) -> str:
    """
    Remove any lines that:
      1. Import or attempt to import the function under test (the LLM often
         emits a commented-out or live import instead of relying on injection).
      2. Are blank comment lines left over after stripping.
    This ensures the injected import is the only authoritative source.
    """
    import re
    cleaned_lines = []
    for line in test_code.splitlines():
        stripped = line.strip()
        # Drop live imports of the function: "from X import func" / "import func"
        if re.search(rf'\bimport\b.*\b{re.escape(function_name)}\b', stripped):
            continue
        # Drop commented-out import hints the LLM often adds as guidance
        if re.match(r'#.*\bimport\b.*\b' + re.escape(function_name) + r'\b', stripped):
            continue
        cleaned_lines.append(line)
    return "\n".join(cleaned_lines)


def prepare_test(test_code: str, function_name: str, file_stem: str = None, use_mutant=False):
    """
    function_name : the real def name inside the source (e.g. 'letter_combinations')
    file_stem     : the source filename without extension (e.g. 'letter_combination_of_phone_numbers')
                    Used for the module path in the import statement.
                    Defaults to function_name when they are the same.
    """
    stem = file_stem if file_stem else function_name
    if use_mutant:
        # Mutant files are named after the real function: letter_combinations_mutant.py
        import_line = f"from mutants.{function_name}_mutant import {function_name}\n\n"
    else:
        # Source files are named after the stem: functions/letter_combination_of_phone_numbers.py
        import_line = f"from functions.{stem} import {function_name}\n\n"

    clean_code = sanitize_test_code(test_code, function_name)
    TEMP_TEST_FILE.write_text(import_line + clean_code, encoding="utf-8")
    return TEMP_TEST_FILE


def ensure_init_files():
    """Ensure functions/ and mutants/ are Python packages so imports resolve."""
    for folder in [FUNCTIONS_FOLDER, MUTANTS_FOLDER]:
        init = folder / "__init__.py"
        if not init.exists():
            init.write_text("", encoding="utf-8")


# -------------------------------
# REDUNDANCY RATE
# -------------------------------
def compute_redundancy_rate(test_code: str) -> float:
    """
    FIX [2]: Compute redundancy rate as per methodology.

    Redundancy = fraction of test methods whose bodies are duplicates of
    another test method in the same suite.

    Strategy: parse the AST, extract the body source of each test_ function,
    normalise it (strip docstrings, collapse whitespace), then count duplicates.
    """
    try:
        tree = ast.parse(test_code)
    except SyntaxError:
        return 0.0

    # Collect all test method bodies (works for both module-level functions
    # and methods inside TestCase classes)
    bodies = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.name.startswith("test"):
                # Serialise the body as a normalised string for comparison
                body_source = ast.dump(ast.Module(body=node.body, type_ignores=[]))
                bodies.append(body_source)

    if len(bodies) <= 1:
        return 0.0

    seen = {}
    duplicate_count = 0
    for body in bodies:
        if body in seen:
            duplicate_count += 1
        else:
            seen[body] = True

    return round(duplicate_count / len(bodies), 4)


# -------------------------------
# RESOLVE TRUE FUNCTION NAME
# -------------------------------
def resolve_function_name(test_file: Path) -> str | None:
    """
    The filename stem (e.g. 'letter_combination_of_phone_numbers') often does
    NOT match the actual def name inside (e.g. 'letter_combinations').
    Strategy:
      1. Derive the source filename from the test filename stem.
      2. Read the source file and extract the first top-level def name.
      3. Fall back to the stem only if the source file cannot be found.
    This ensures imports, coverage scoping, and mutant lookup all use the
    real function name rather than the file's display name.
    """
    import re
    file_stem = test_file.stem.split("_run")[0]

    if file_stem == "__init__":
        return None

    # Look up the matching source file in functions/
    source_file = FUNCTIONS_FOLDER / f"{file_stem}.py"
    if source_file.exists():
        code = source_file.read_text(encoding="utf-8")
        match = re.search(r'^def (\w+)\(', code, re.MULTILINE)
        if match:
            return match.group(1)

    # Fallback: use the stem (handles the 4 correctly-named files)
    return file_stem


# -------------------------------
# EVALUATE SINGLE TEST FILE
# -------------------------------
def evaluate_test(test_file: Path):
    # Resolve the true function name from the source file, not the filename
    function_name = resolve_function_name(test_file)
    if function_name is None:
        return None  # Skip __init__ and unresolvable files

    # The source file stem (used for coverage path and source import)
    file_stem = test_file.stem.split("_run")[0]

    test_code = test_file.read_text(encoding="utf-8")

    # Original run — import uses function_name, coverage uses file_stem
    temp_file = prepare_test(test_code, function_name, file_stem=file_stem, use_mutant=False)
    executable, passed, line_cov, branch_cov, output = run_pytest(temp_file, file_stem)

    # Mutation run — mutant files are named after the real function name
    mutation_killed = False
    mutant_file = MUTANTS_FOLDER / f"{function_name}_mutant.py"
    if mutant_file.exists():
        temp_file = prepare_test(test_code, function_name, file_stem=file_stem, use_mutant=True)
        m_exec, m_passed, _, _, _ = run_pytest(temp_file, file_stem)
        if m_exec and not m_passed:
            mutation_killed = True
    else:
        print(f"         ⚠ No mutant for '{function_name}' ({file_stem})")

    redundancy_rate = compute_redundancy_rate(test_code)

    return {
        "file": str(test_file),
        "function": function_name,
        "file_stem": file_stem,
        "executable": executable,
        "passed": passed,
        "line_coverage": line_cov,
        "branch_coverage": branch_cov,
        "mutation_killed": mutation_killed,
        "redundancy_rate": redundancy_rate,
        "output": output
    }


# -------------------------------
# AVERAGE 3 RUNS PER FUNCTION-PROMPT PAIR
# -------------------------------
def average_runs(file_results: list) -> list:
    """
    FIX [3]: Methodology states results are averaged across 3 runs.
    Group _run1 / _run2 / _run3 files by function name, then average
    all numeric metrics. Boolean metrics (executable, mutation_killed)
    are majority-voted.
    """
    groups = defaultdict(list)
    for r in file_results:
        func = r["function"]  # already stripped of _runN by evaluate_test
        groups[func].append(r)

    averaged = []
    for func, runs in groups.items():
        n = len(runs)
        avg = {
            "function": func,
            "runs": n,
            # Executability: majority vote across runs
            "executable": sum(r["executable"] for r in runs) > n / 2,
            # Passed: majority vote
            "passed": sum(r["passed"] for r in runs) > n / 2,
            # Mutation killed: majority vote (consistent with how mutation score
            # is defined — if ≥2 of 3 runs kill the mutant, we count it as killed)
            "mutation_killed": sum(r["mutation_killed"] for r in runs) > n / 2,
            # Numeric metrics: true averages
            "line_coverage": round(sum(r["line_coverage"] for r in runs) / n, 2),
            "branch_coverage": round(sum(r["branch_coverage"] for r in runs) / n, 2),
            "redundancy_rate": round(sum(r["redundancy_rate"] for r in runs) / n, 4),
        }
        averaged.append(avg)

    return averaged


# -------------------------------
# MAIN EVALUATION
# -------------------------------
def evaluate():
    ensure_init_files()  # Guarantee package imports work
    if not OUTPUT_FOLDER.exists():
        print("❌ Output folder not found")
        return

    results = {}

    for model_dir in OUTPUT_FOLDER.iterdir():
        if not model_dir.is_dir():
            continue

        model_name = model_dir.name
        results[model_name] = {}
        print(f"\n🤖 Model: {model_name}")

        for prompt_dir in model_dir.iterdir():
            if not prompt_dir.is_dir():
                continue

            prompt_name = prompt_dir.name
            print(f"   🔹 Prompt: {prompt_name}")

            py_files = list(prompt_dir.glob("*.py"))

            # Collect raw per-file results
            raw_file_results = []
            for test_file in py_files:
                print(f"      ▶ {test_file.name}")
                res = evaluate_test(test_file)
                if res is not None:
                    raw_file_results.append(res)

            # FIX [3]: Average across the 3 runs per function
            averaged = average_runs(raw_file_results)

            num_functions = len(averaged)

            # Aggregate over averaged function results
            executable_count = sum(1 for r in averaged if r["executable"])
            passed_count = sum(1 for r in averaged if r["passed"])
            # FIX [4]: Mutation score denominator = number of unique functions,
            # NOT total files. This matches the methodology.
            killed_count = sum(1 for r in averaged if r["mutation_killed"])

            avg_line_cov = round(
                sum(r["line_coverage"] for r in averaged) / num_functions, 2
            ) if num_functions else 0

            avg_branch_cov = round(
                sum(r["branch_coverage"] for r in averaged) / num_functions, 2
            ) if num_functions else 0

            avg_redundancy = round(
                sum(r["redundancy_rate"] for r in averaged) / num_functions, 4
            ) if num_functions else 0

            results[model_name][prompt_name] = {
                "total_functions": num_functions,
                "passed": passed_count,
                "failed": num_functions - passed_count,
                "executable": executable_count,
                # FIX [4]: mutation_killed / total_functions (not total files)
                "mutation_killed": killed_count,
                "avg_line_coverage": avg_line_cov,
                "avg_branch_coverage": avg_branch_cov,
                # FIX [2]: Redundancy rate now computed and stored
                "avg_redundancy_rate": avg_redundancy,
                "function_results": averaged,
            }

    RESULTS_FILE.write_text(json.dumps(results, indent=2))

    # ---------------- SUMMARY ----------------
    print("\n📊 SUMMARY")
    print("=" * 60)

    for model in results:
        print(f"\n🤖 {model}")
        for prompt, stats in results[model].items():
            total = stats["total_functions"]
            passed = stats["passed"]
            execs = stats["executable"]
            killed = stats["mutation_killed"]
            line_cov = stats["avg_line_coverage"]
            branch_cov = stats["avg_branch_coverage"]
            redundancy = stats["avg_redundancy_rate"]

            pass_rate = (passed / total * 100) if total else 0
            exec_rate = (execs / total * 100) if total else 0
            # FIX [4]: mutation score = killed / unique functions × 100
            mutation_score = (killed / total * 100) if total else 0

            print(f"\n   {prompt}:")
            print(f"      Functions evaluated : {total}")
            print(f"      Executability       : {execs}/{total} ({exec_rate:.1f}%)")
            print(f"      Pass rate           : {passed}/{total} ({pass_rate:.1f}%)")
            print(f"      Mutation score      : {killed}/{total} ({mutation_score:.1f}%)")
            print(f"      Avg line coverage   : {line_cov}%")
            print(f"      Avg branch coverage : {branch_cov}%")
            print(f"      Avg redundancy rate : {redundancy:.2%}")

    print(f"\n📁 Results saved to {RESULTS_FILE}")


if __name__ == "__main__":
    evaluate()