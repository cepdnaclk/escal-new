import requests

def takeStaffDetails(tag):
    API_URL = f"https://api.ce.pdn.ac.lk/people/v1/staff/{tag}/"
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        staff_details = {
            "name": data["name"],
            "designation": data["designation"],
            "profile_image": data["profile_image"],
            "profile_url": data["profile_url"]
        }
        return staff_details
    else:
        return None

def createStaffDictionary(staffTags):
    all_staff_details = []
    for tag in staffTags:
        details = takeStaffDetails(tag)
        if details:
            all_staff_details.append(details)
    return all_staff_details
