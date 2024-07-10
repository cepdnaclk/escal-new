import requests

# 1. Extract 3YP Projects

def extractTeamInProject(API):
    response = requests.get(API)
    if response.status_code == 200:
        project = response.json()
        teamDetails = project.get("team")
        if teamDetails is not None:
            return teamDetails
        return None
    
def extract3ypProjectsFromBatch(batch):
    API_URL = f"https://api.ce.pdn.ac.lk/projects/v1/3yp/{batch}/"
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()

        #Add Team Details
        for item_key, item_value in data.items():
            projectAPI = item_value["api_url"]
            item_value["team"] = extractTeamInProject(projectAPI)
        return data
    return None
    
def findBatches():
    API_URL = "https://api.ce.pdn.ac.lk/projects/v1/3yp"
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        batches = data["batches"].keys()
        keys = list(batches)
        keys.reverse()
        return keys
    else:
        return None

# 2. Extract Projects based on tags

def get_embedded_system_projects(api_url, tags):
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
            return None
    except requests.exceptions.RequestException as e:
        return None

# ~~ Main Code ~~
def createProjectsDictionary(projectTags):
    all_Projects = {}

    #Find batches with 3yp projects
    batchesWith3ypProjects = findBatches()
    first_part = batchesWith3ypProjects[:2]
    second_part = batchesWith3ypProjects[2:]

    # Extract all the 3yp Projects - New
    for batch in first_part:
        batch3ypProjects = extract3ypProjectsFromBatch(batch)
        all_Projects.update(batch3ypProjects)
        print(f"\t a) Extracted 3yp data of batch {batch}")

    # Extract Projects from tags   
    api_url = "https://api.ce.pdn.ac.lk/projects/v1/filter/tags/"
    embedded_system_projects = get_embedded_system_projects(api_url, projectTags)

    if embedded_system_projects:
        for projects in embedded_system_projects.values():
            for project in projects:
                if project['category']['code'] != '3yp':
                    key = project['title']
                    projectAPI = project["api_url"]           
                    project["team"] = extractTeamInProject(projectAPI)
                    all_Projects.update({key:project})
        print("\t b) Extracted projects based on tags")

    # Extract all the 3yp Projects - Old
    for batch in second_part:
        batch3ypProjects = extract3ypProjectsFromBatch(batch)
        all_Projects.update(batch3ypProjects)
        print(f"\t c) Extracted 3yp data of batch {batch}")
        
    return all_Projects 
