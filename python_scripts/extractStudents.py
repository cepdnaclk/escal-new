import requests
import json

file_path = "../_data/students.json"

#Extract projects based on tag ex: 3yp
def takeProjectDetailsBasedOnTag(tag):
    API_URL = f"https://api.ce.pdn.ac.lk/projects/v1/{tag}/"
    response = requests.get(API_URL)
    if response.status_code == 200:

        # Parse the JSON response
        data = response.json()

        #Take the dictionary containing batches
        batchesDictionary = data["batches"]

        #Take the batches(E14,E15,...) to a list
        batches = list( batchesDictionary.keys() )
        batches.reverse()

        batchProjectsURL = []
        for batch in batches:
            batchProjectsURL.append( batchesDictionary[batch]["api_url"] ) 
            
        return batchProjectsURL
    
    else:
        return None

def takeDataFromCategoryBatchProject(category, project, batch):
     API_URL = f"https://api.ce.pdn.ac.lk/projects/v1/{category}/{batch}/{project}/"
     response = requests.get(API_URL)
     if response.status_code == 200:
         data = response.json()
         
         if "team" in data:
             projectTeams = list(data["team"].keys() )
         else:
             projectTeams = []
                 
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
      
def createStudentJSONFile(tag):
    APIlist = takeProjectDetailsBasedOnTag(tag)  #ex: "https://api.ce.pdn.ac.lk/projects/v1/3yp/E18/

    projectNames = [] #To hold project names -> ex: e18-3yp-Automated-Mini-Greenhouse-Monitoring-And-Control-System

    for api in APIlist:
     response = requests.get(api) #Ex: Take data from"https://api.ce.pdn.ac.lk/projects/v1/3yp/E18/" URL
     if response.status_code == 200:
         data = response.json()
         projectNames.append( list( data.keys() ) )  #Extract the Keys. ex: e18-3yp-Automated-Mini-Greenhouse-Monitoring-And-Control-System

    extracted_parts = [] #To hold --> ex: ("E18","3yp","Automated-Mini-Greenhouse-Monitoring-And-Control-System")

    for year_list in projectNames:
        for project in year_list:
            parts = project.split('-')
            if len(parts) >= 3 and parts[1] == tag :
                year = parts[0].capitalize()
                t3yp = parts[1]
                project_name = '-'.join(parts[2:])
                extracted_parts.append((year, t3yp, project_name))

    file_path = "../_data/student.json"

    allStudentDetails = [] #File To write all student details
    
    for project in extracted_parts:
        teamlist = takeDataFromCategoryBatchProject(project[1], project[2], project[0])  # Take team list as ["E/YY/XXX,"E/YY/XXX","E/YY/XXX}]
        for member in teamlist:
            if takeStudentDetails(member) == None:
                print("SKIP")
            else:
                allStudentDetails.append( takeStudentDetails(member) )
      
    with open(file_path, "w") as json_file:
        json.dump(allStudentDetails, json_file, indent=4)
    print("Done ") 

