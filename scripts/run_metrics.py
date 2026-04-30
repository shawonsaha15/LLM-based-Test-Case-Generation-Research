import os, subprocess, csv

function_folder = "../functions/"
test_folders = ["../generated_tests/zero_shot",
                "../generated_tests/few_shot",
                "../generated_tests/structured",
                "../generated_tests/cot"]

mutant_folder = "../mutants/"
results_file = "../metrics/results.csv"

os.makedirs("../metrics/", exist_ok=True)

def measure_coverage(test_file):
    try:
        # run coverage for this test file
        res = subprocess.run(
            ["coverage", "run", "-m", "unittest", test_file],
            capture_output=True,
            text=True
        )
        # get percentage from coverage report
        subprocess.run(["coverage", "report"], capture_output=True, text=True)
        # for simplicity, success/fail
        success = res.returncode == 0
        return success
    except Exception:
        return False

def measure_mutation(test_file, mutants):
    killed = 0
    for mutant in mutants:
        try:
            res = subprocess.run(
                ["coverage", "run", "-m", "unittest", test_file, mutant],
                capture_output=True,
                text=True
            )
            if res.returncode != 0:
                killed += 1
        except:
            pass
    return killed / max(len(mutants),1)

with open(results_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Function", "Prompt", "Run", "ExecSuccess", "MutationScore"])
    
    for folder in test_folders:
        prompt_type = os.path.basename(folder)
        for test_file in os.listdir(folder):
            test_path = os.path.join(folder, test_file)
            # Executability
            exec_success = measure_coverage(test_path)
            # Mutation score
            mutants = [os.path.join(mutant_folder, m) for m in os.listdir(mutant_folder)]
            mutation_score = measure_mutation(test_path, mutants)
            writer.writerow([test_file, prompt_type, test_file[-5], exec_success, mutation_score])