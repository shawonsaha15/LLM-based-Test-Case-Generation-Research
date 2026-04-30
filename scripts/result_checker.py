import os
import json
import pandas as pd

def process_json_file(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)

    summary_rows = []
    function_rows = []

    for model_name, model_data in data.items():
        if isinstance(model_data, dict):
            for variant, variant_data in model_data.items():

                # Case 1: direct metrics
                if isinstance(variant_data, dict) and "total_functions" in variant_data:
                    summary_rows.append({
                        "file": os.path.basename(filepath),
                        "model": model_name,
                        "variant": variant,
                        **{k: v for k, v in variant_data.items() if k != "function_results"}
                    })

                    for func in variant_data.get("function_results", []):
                        function_rows.append({
                            "file": os.path.basename(filepath),
                            "model": model_name,
                            "variant": variant,
                            **func
                        })

                # Case 2: nested (cot, few_shot, etc.)
                elif isinstance(variant_data, dict):
                    for sub_variant, sub_data in variant_data.items():
                        if isinstance(sub_data, dict) and "total_functions" in sub_data:
                            summary_rows.append({
                                "file": os.path.basename(filepath),
                                "model": model_name,
                                "variant": sub_variant,
                                **{k: v for k, v in sub_data.items() if k != "function_results"}
                            })

                            for func in sub_data.get("function_results", []):
                                function_rows.append({
                                    "file": os.path.basename(filepath),
                                    "model": model_name,
                                    "variant": sub_variant,
                                    **func
                                })

    return summary_rows, function_rows


def process_folder(folder_path, output_prefix="output"):
    all_summary = []
    all_functions = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            filepath = os.path.join(folder_path, filename)
            summary, functions = process_json_file(filepath)
            all_summary.extend(summary)
            all_functions.extend(functions)

    # Convert to DataFrames
    df_summary = pd.DataFrame(all_summary)
    df_functions = pd.DataFrame(all_functions)

    # Save as CSV
    df_summary.to_csv(f"{output_prefix}_summary.csv", index=False)
    df_functions.to_csv(f"{output_prefix}_functions.csv", index=False)

    print(f"Saved:\n- {output_prefix}_summary.csv\n- {output_prefix}_functions.csv")


# 🔧 Usage
folder_path = r"D:\Research\SQA\results\Fifth_Tests"
process_folder(folder_path)