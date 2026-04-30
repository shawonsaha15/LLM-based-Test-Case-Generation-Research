import subprocess
import json
from pathlib import Path

OUTPUT_FOLDER = Path(r"D:\Research\SQA\generated_tests\llama-3.3-70b-versatile")
RESULTS_FILE = Path("results.json")

def run_pytest_on_file(test_file: Path):
    try:
        result = subprocess.run(
            ["pytest", str(test_file), "--maxfail=1", "--disable-warnings", "-q"],
            capture_output=True,
            text=True,
            timeout=20
        )

        passed = result.returncode == 0

        return {
            "file": str(test_file),
            "passed": passed,
            "output": result.stdout + result.stderr
        }

    except Exception as e:
        return {
            "file": str(test_file),
            "passed": False,
            "output": str(e)
        }


def evaluate():
    if not OUTPUT_FOLDER.exists():
        print(f"❌ ERROR: Output folder {OUTPUT_FOLDER} does not exist.")
        return

    results = {}

    print(f"🔍 Starting evaluation in: {OUTPUT_FOLDER}\n")

    for prompt_type in OUTPUT_FOLDER.iterdir():
        if not prompt_type.is_dir():
            continue

        print(f"▶ Processing prompt folder: {prompt_type.name}")

        py_files = list(prompt_type.glob("*.py"))
        if not py_files:
            print(f"   ⚠ No test files found in {prompt_type.name}")
            continue

        results[prompt_type.name] = {
            "total": 0,
            "passed": 0,
            "failed": 0,
            "files": []
        }

        for test_file in py_files:
            print(f"   Running pytest on: {test_file.name}")
            res = run_pytest_on_file(test_file)

            results[prompt_type.name]["total"] += 1
            if res["passed"]:
                results[prompt_type.name]["passed"] += 1
            else:
                results[prompt_type.name]["failed"] += 1

            results[prompt_type.name]["files"].append(res)

    # Save results
    RESULTS_FILE.write_text(json.dumps(results, indent=2))

    print("\n📊 Evaluation Summary:\n")

    for k, v in results.items():
        total = v["total"]
        passed = v["passed"]
        score = (passed / total * 100) if total else 0

        print(f"{k}: {passed}/{total} passed ({score:.1f}%)")

    print(f"\n📁 Detailed results saved to {RESULTS_FILE}")


if __name__ == "__main__":
    evaluate()