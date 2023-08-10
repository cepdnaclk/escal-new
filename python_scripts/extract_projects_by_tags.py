import requests
import json
import os

def get_embedded_system_projects(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            projects_data = response.json()
            embedded_system_projects = {}

            for category, projects in projects_data.items():
                if "Embedded Systems" in category:
                    embedded_system_projects[category] = projects

            return embedded_system_projects
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def append_to_json_file(data, output_filename):
    try:
        if os.path.exists(output_filename):
            with open(output_filename, 'r') as json_file:
                existing_data = json.load(json_file)
        else:
            existing_data = []

        existing_data.extend(data)

        with open(output_filename, 'w') as json_file:
            json.dump(existing_data, json_file, indent=4)

        print(f"Data appended to {output_filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    api_url = "https://api.ce.pdn.ac.lk/projects/v1/filter/tags/"
    output_directory = r"D:\ESCAL\escal-new\_data"
    os.makedirs(output_directory, exist_ok=True)  # Create the output directory if it doesn't exist
    output_filename = os.path.join(output_directory, "output.json")

    embedded_system_projects = get_embedded_system_projects(api_url)

    if embedded_system_projects:
        projects_list = []
        for projects in embedded_system_projects.values():
            for project in projects:
                if "3yp" not in project.get("category", {}).get("code", "").lower():
                    projects_list.append(project)

        append_to_json_file(projects_list, output_filename)
    else:
        print("No embedded system projects found.")
