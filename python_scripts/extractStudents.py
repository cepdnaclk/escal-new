import requests
import json

def takeDataFromAPIURL(API_URL):
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

#Sort based on E number
def custom_sort(item):
    parts = item.split('/')
    return int(parts[1]), int(parts[2]) 


# ~~~~~~ Main Code ~~~~~~~~~

def createStudentsDictionary(input_file_path, output_file_path):
     allStudentDetails = []
     teamlist = []
     
     # Open the JSON file in read mode
     with open(input_file_path, 'r') as json_file:
         data = json.load(json_file)

     for project_key, project_info in data.items():
         code = project_info['category']['code']
    
         if code != '3yp':
             API_URL = project_info['api_url']
             data = takeDataFromAPIURL( API_URL )
        
             if data == []:
                 continue   # Skip details when team details are not present
             else:
                 for enumber in data:
                     teamlist.append(enumber)

     # Remove duplicates
     unique_list = list(set(teamlist))

     # Convert the set back to a list to maintain the order
     sorted_data = sorted(unique_list, key=custom_sort)
     sorted_data.reverse()

     for member in sorted_data:
         allStudentDetails.append( takeStudentDetails(member) )
     return allStudentDetails
