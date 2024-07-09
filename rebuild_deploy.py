import os
import json
from python_scripts.extractStaff import createStaffDictionary

# File paths
staff_json_file_path = '_data/staff.json'

# 1. Extract Staff Data
staffTags = ["roshanr", "isurunawinne", "swarnar"]
staff_data = createStaffDictionary(staffTags)
os.makedirs(os.path.dirname(staff_json_file_path), exist_ok=True) # Ensure the directory exists

# Write the data to the JSON file
with open(staff_json_file_path, "w") as json_file:
    json.dump(staff_data, json_file)
#print("JSON file generated successfully.")

# 2. Extract Projects

# 3. Extract Students
