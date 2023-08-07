import requests
import json



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

            existing_data.append(data)

            if data not in existing_data:
                with open(output_filename, 'w') as json_file:
                    json.dump(existing_data, json_file, indent=4)
                print(f"Data fetched and appended to {output_filename}")
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    category_id = input("Enter CategoryID: ")
    batch_ids = ["E17","E16", "E15", "E14"]
    output_filename = "output_data.json"
    for batch_id in batch_ids:
        fetch_and_append_data(category_id, batch_id, output_filename)
