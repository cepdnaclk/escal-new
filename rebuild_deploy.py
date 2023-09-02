import os
from python_scripts.extract_projects import *
from python_scripts.generate_subpages import *
from python_scripts.extractStaff import *
from python_scripts.extractStudents import *

filters = ['co328', '2yp', 'co542', 'co226', 'co227']
key_tags = ['embedded', '3yp', 'embedded-systems', 'embedded-system', 'iot', 'arduino', 'fpga', 'raspberry', 'robot', 'robotics', 'gpu', 'bio-medical', 'swarm', 'nvidia']
DATA_PATH = './_data'
PAGES_PATH = './pages'

# Extract and generate data.
extract_projects('https://api.ce.pdn.ac.lk/projects/v1/', f'{DATA_PATH}/all_projects.json', key_only=True)
extract_projects('https://api.ce.pdn.ac.lk/projects/v1/', 
                f'{DATA_PATH}/projects.json', 
                f'{DATA_PATH}/excluded_projects.json', 
                filters,
                key_tags)
save_excluded_projects(f'{DATA_PATH}/all_projects.json', f'{DATA_PATH}/projects.json', f'{DATA_PATH}/excluded_projects.json')
extract_categories('https://api.ce.pdn.ac.lk/projects/v1/', f'{DATA_PATH}/project_categories.json', f'{DATA_PATH}/projects.json')

# Generate subpages.
generate_category_pages(f'{DATA_PATH}/project_categories.json', f'{PAGES_PATH}/projects')

#Create staff.json file with staff Details
staffTags = ["roshanr", "isurunawinne", "swarnar"]
createStaffDictionary(staffTags)

# Create student.json file with staff Details
# createStudentJSONFile("3yp")