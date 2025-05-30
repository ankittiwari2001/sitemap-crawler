import os
import json

def merge_json_files_in_dir(directory):
    merged_data = []
    
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory.")
        return

    json_files = [f for f in os.listdir(directory) if f.endswith(".json")]
    if not json_files:
        print("No JSON files found in the directory.")
        return

    print(f"Found {len(json_files)} JSON file(s) in '{directory}'")

    for filename in json_files:
        filepath = os.path.join(directory, filename)
        try:
            with open(filepath, "r") as f:
                data = json.load(f)
                if isinstance(data, list):
                    merged_data.extend(data)
                else:
                    merged_data.append(data)
        except Exception as e:
            print(f"Error reading {filename}: {e}")

    output_file = "merged_output.json"
    with open(output_file, "w") as f:
        json.dump(merged_data, f, indent=2)

    print(f"\n✅ Merged {len(json_files)} file(s) into '{output_file}' with {len(merged_data)} total entries.")

if __name__ == "__main__":
    dir_path = input("Enter the directory containing JSON files: ").strip()
    merge_json_files_in_dir(dir_path)
