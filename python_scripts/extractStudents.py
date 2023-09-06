import requests
import json

def takeDataFromCategoryBatchProject(category, title, batch):
     API_URL = f"https://api.ce.pdn.ac.lk/projects/v1/{category}/{batch}/{title}/"
     response = requests.get(API_URL)
     if response.status_code == 200:
         data = response.json()
         
         if "team" in data:
             projectTeams = list(data["team"].keys() )  # There are projects, with no team details
         else:
             projectTeams = []# If team details are not present, return []
                 
         return projectTeams
     else:
         return None

def takeStudentDetails(eNumber):
    parts = eNumber.split('/')
    batch = parts[0] + parts[1]  # Concatenate 'E' and 'xx' to get 'Exx'
    number = parts[2]
    API_URL = f"https://api.ce.pdn.ac.lk/people/v1/students/{batch}/{number}/"
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()

        #Extract Necessary Data
        name = data["preferred_long_name"]
        
        if name == "":
            name = data["name_with_initials"]
        if name == "":
            name = data["full_name"]
            
        profileImage = data["profile_image"]
        profileURL = data["profile_page"]
        
        student_details = {
            "name": name,
            "profile_image": profileImage,
            "profile_url": profileURL,
            "batch": batch
        }

        return student_details
        
    else:
        return None

# Main Code
# Projects json file location 
input_file_path = '../_data/projects.json'
output_file_path = "../_data/student.json"
allStudentDetails = []
teamlist = []

# Open the JSON file in read mode
with open(input_file_path, 'r') as json_file:
    data = json.load(json_file)

for project_key, project_info in data.items():
    code = project_info['category']['code']
    
    if code != '3yp':
        components = project_key.split('-')
        batch = components[0].capitalize()  # Exx
        category = components[1]               
        title = '-'.join(components[2:])
        
        data = takeDataFromCategoryBatchProject(category, title, batch)
        if data == []:
            continue   # Skip details when team details are not present
        else:
            for enumber in data:
                teamlist.append(enumber)

teamlist.reverse()        

# Remove duplicates
unique_list = list(set(teamlist))

# Convert the set back to a list to maintain the order
unique_list = sorted(unique_list, key=teamlist.index)

print(unique_list)

for member in unique_list:
    allStudentDetails.append( takeStudentDetails(member) )

with open(output_file_path, "w") as json_file:
    json.dump(allStudentDetails, json_file, indent=4)


