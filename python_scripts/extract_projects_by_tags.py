import requests
import json
import os

tags = ["Embedded Systems", "FPGA", "Computer Architecture"]
def get_embedded_system_projects(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            projects_data = response.json()
            embedded_system_projects = {}

            for category, projects in projects_data.items():
                for tag in tags:    
                    if tag in category:
                        embedded_system_projects[category] = projects

            return embedded_system_projects
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def add_to_json_file(data, output_filename):
    #print(type(data))
    
    #print(page_api)
    try:
        if os.path.exists(output_filename):
            with open(output_filename, 'r') as json_file:
                existing_data = json.load(json_file)
                
        else:
            existing_data = {}

        # Check if each project is already in the existing data
        for project in data:
            if project not in existing_data:
                key =  project
                value = data[project]
                page_api = value["api_url"]
                repo_url = value["repo_url"]
                # Split the URL by "https://github.com/cepdnaclk/"
                parts = repo_url.split("https://github.com/cepdnaclk/")
                # print(repo_url)


                # Check if the URL matches the expected format
                # print(len(parts))
                if len(parts) == 2:
                    desired_part = parts[1]
                    #print(desired_part)
                    github_url = "https://api.github.com/repos/cepdnaclk/" + desired_part
                    response_github = requests.get(github_url)
                    print(response_github.status_code)
                    if response_github.status_code == 200:
                        github_data = response_github.json()
                        #print(github_data)
                        value['stargazers_count'] = github_data['stargazers_count']
                        value['updated_at'] = github_data['updated_at']
                else:
                    print("URL format is not as expected.")
                # print(page_api)
                response_page = requests.get(page_api)
                if response_page.status_code == 200:
                    project_data = response_page.json()
                    team_members = {}
                    
                    for e_nmumber, values in project_data['team'].items():
                        student = project_data['team'][e_nmumber]
                        name = student["name"]
                        student_url = student["api_url"]
                        team_member_details = {"name":name,
                                               "api_url":student_url}
                        team_members[e_nmumber] = team_member_details
                    value["team"] = team_members

                existing_data.update({key:value})
                #print(project)

        with open(output_filename, 'w') as json_file:
            json.dump(existing_data, json_file, indent=4)

        print(f"Data appended to {output_filename}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    api_url = "https://api.ce.pdn.ac.lk/projects/v1/filter/tags/"
    output_directory = r"_data"
    os.makedirs(output_directory, exist_ok=True)  # Create the output directory if it doesn't exist
    output_filename = os.path.join(output_directory, "project.json")

    embedded_system_projects = get_embedded_system_projects(api_url)
    #print(embedded_system_projects)

    if embedded_system_projects:
        projects_list = {}
        for projects in embedded_system_projects.values():
            for project in projects:
                key = project['title']
                projects_list.update({key:project})
                #print(projects_list)
                
        print()
        add_to_json_file(projects_list, output_filename)
    else:
        print("No embedded system projects found.")
