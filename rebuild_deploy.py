import os
import json
from python_scripts.extractStaff import createStaffDictionary
from python_scripts.extractProjects import createProjectsDictionary

# File paths
staff_json_file_path = '_data/staff.json'
projects_json_file_path = '_data/projects.json'

# 1. Extract Staff Data
staffTags = ["roshanr", "isurunawinne", "swarnar"]
staff_data = createStaffDictionary(staffTags)

# Write the data to the JSON file
print("Generating Staff Data............")
with open(staff_json_file_path, "w") as json_file:
    json.dump(staff_data, json_file)
print("\t Staff JSON file generated \n")

# 2. Extract Projects
print("Generating Projects Data............")

projectTags = ["Embedded Systems", "FPGA", "Computer Architecture"]
projects_data = createProjectsDictionary(projectTags)

with open(projects_json_file_path, "w") as json_file:
    json.dump(projects_data, json_file, indent=4)
print("\t Projects JSON file generated \n")

# 3. Extract Students

