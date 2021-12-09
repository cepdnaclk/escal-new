import os
from python_scripts.extract_projects import *
from python_scripts.generate_subpages import *

filters = ['co328', '2yp', 'co542', 'co226']
key_tags = ['embedded', 'embedded-systems', 'robot', 'robotics', 'gpu', 'bio-medical', 'swarm', 'nvidia']
DATA_PATH = './_data'
PAGES_PATH = './pages'

# Extract and generate data.
extract_projects('https://cepdnaclk.github.io/api.ce.pdn.ac.lk/projects/', f'{DATA_PATH}/all_projects.json', key_only=True)
save_excluded_projects(f'{DATA_PATH}/all_projects.json', f'{DATA_PATH}/projects.json', f'{DATA_PATH}/excluded_projects.json')
extract_projects('https://cepdnaclk.github.io/api.ce.pdn.ac.lk/projects/', 
                f'{DATA_PATH}/projects.json', 
                f'{DATA_PATH}/excluded_projects.json', 
                filters,
                key_tags)
extract_categories('https://cepdnaclk.github.io/api.ce.pdn.ac.lk/projects/', f'{DATA_PATH}/project_categories.json', f'{DATA_PATH}/projects.json')

# Generate subpages.
generate_category_pages(f'{DATA_PATH}/project_categories.json', f'{PAGES_PATH}/projects')

# Copy /_data/projects.json to /data/projects.json
os.system(f'cp {DATA_PATH}/projects.json ./data/projects.json')