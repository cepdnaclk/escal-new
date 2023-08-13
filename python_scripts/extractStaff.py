import requests
import json

file_path = "../_data/staff.json"

def takeStaffDetails(tag):
    API_URL = f"https://api.ce.pdn.ac.lk/people/v1/staff/{tag}/"
    response = requests.get(API_URL)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Take the Necessary Values
        name = data["name"]
        designation = data["designation"]
        profileImage = data["profile_image"]
        profileURL = data["profile_url"]

        # Create a dictionary to hold the staff details
        staff_details = {
            "name": name,
            "designation": designation,
            "profile_image": profileImage,
            "profile_url": profileURL
        }

        return staff_details
        
    else:
        # print(f"Failed to retrieve data for {tag}. Status code: {response.status_code}")
        return None


# List to hold all staff detail dictionaries
all_staff_details = []

def createStaffDictionary(staffTags):
    # Loop through the staff tags and retrieve details for each staff member
    for tag in staffTags:
        details = takeStaffDetails(tag)
        if details:
            all_staff_details.append(details)
        
    # Write all staff details to a JSON file --> location is given as file_path
    with open(file_path, "w") as json_file:
        json.dump(all_staff_details, json_file, indent=4)