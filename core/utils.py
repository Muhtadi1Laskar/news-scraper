import json
import os


def save_data(data, website_name):
    file_path = f"Data/{website_name}.json"

    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    try:
        with open(file_path, 'r') as f:
            existing_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []

    existing_data.extend(data)  # Append new data to the existing list

    with open(file_path, 'w') as f:
        json.dump(existing_data, f, indent=4)
