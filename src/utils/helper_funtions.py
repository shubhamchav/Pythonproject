import os
import json


def load_db_config():
    # Print the current working directory to verify where Python is looking
    print("Current working directory:", os.getcwd())

    # Construct the absolute path to the db_config.json file
    json_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resources', 'db_config.json'))

    # Print the constructed path to verify correctness
    print("Constructed json file path:", json_file_path)

    try:
        with open(json_file_path, 'r') as fr:
            content = json.load(fr)
            return content
    except FileNotFoundError:
        print(f"Error: File '{json_file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from the file '{json_file_path}'.")
        return None
