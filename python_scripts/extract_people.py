import json, requests
from requests import api

FILE_NAME = 'people.json'
API = "https://api.ce.pdn.ac.lk/people/v1/"
data = ["honorific", "preferred_long_name", "emails", "profile_image", "urls"]

# clear the file
def clearJSON():
    with open(FILE_NAME, 'a') as f:
        f.seek(0)
        f.truncate()

# extracts data
def extractData(request):
    temp = {}
    personJSON = request.json()

    for item in data:
        if item == "emails":
            temp[item] = personJSON[item]['faculty']

        elif item == "urls":
            temp['linkedin'] = personJSON[item]['linkedin']
            temp['website'] = personJSON[item]['website']

        else:
            temp[item] = personJSON[item]

    return temp

def extractPeople():
    # read from people.txt
    with open('people.txt', 'r') as f:
        people = f.read().splitlines()
        peopleJSON = []
        for person in people:
            # checks whether the person is a student or a staff member
            # if '@' in person:
            #     request = requests.get(API + 'staff/' + person)

            # split faculty id
            faculty, batch, number = person.split('/')
            # send request
            request = requests.get(API + 'students/' + faculty + batch + '/' + number)

            # if request is successful
            if request.status_code == 200:
                peopleJSON.append(extractData(request))

    return peopleJSON

# The people associated with ESCAL should be manually added to the people.txt file
#   - If the individual is a student, the registration number is added
#   - If the individual is a staff member the email address (depends on the paramter decided by the API developers) is added
# The most abridged data ["honorific", "preferred_long_name", "emails", "profile_image", "urls"] is included at the moment

if __name__ == "__main__":
    # copy data in people.json to a list
    # with open(FILE_NAME, "rb+") as f:
    #     people_backup = json.load(f)

    clearJSON()
    peopleJSON = extractPeople()

    # write to json file
    # with open('people.json', 'a') as f:
    #     if peopleJSON:
    #         json.dump(peopleJSON, f, indent=4)
    #     else:
    #         json.dump(people_backup, f, indent=4)

    with open(FILE_NAME, 'a') as f:
        json.dump(peopleJSON, f, indent=4)


    