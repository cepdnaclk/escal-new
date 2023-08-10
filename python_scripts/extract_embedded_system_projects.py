import requests
import json
import os

def fetch_and_append_data(category_id, batch_id, output_filename):
    try:
        api_url = f"https://api.ce.pdn.ac.lk/projects/v1/{category_id}/{batch_id}"
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()

            try:
                with open(output_filename, 'r') as json_file:
                    existing_data = json.load(json_file)
            except FileNotFoundError:
                existing_data = []

            if data not in existing_data:
                existing_data.append(data)
                with open(output_filename, 'w') as json_file:
                    json.dump(existing_data, json_file, indent=4)
                print(f"Data fetched and appended to {output_filename}")
            else:
                print("Data is already present in the JSON file.")
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    category_id = "3yp"
    batch_ids = ["E17", "E16", "E15", "E14"]
    output_directory = "D:\ESCAL\escal-new\_data"
    os.makedirs(output_directory, exist_ok=True)  # Create the output directory if it doesn't exist
    output_filename = os.path.join(output_directory, "output.json")

    # Fetch and append data for each batch ID
    for batch_id in batch_ids:
        fetch_and_append_data(category_id, batch_id, output_filename)
