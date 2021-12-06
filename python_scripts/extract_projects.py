import requests
import json
from tqdm import tqdm

# Use to extract data from the API.
def extract_projects(url, filename, excluded_filename=None, filters=[], key_tags=[], key_only=False):
    try:
        with open(filename, 'r') as f:
            all_projects = json.load(f)
    except:
        all_projects = {}

    try:
        with open(excluded_filename, 'r') as f:
            excluded_projects = json.load(f)
    except:
        excluded_projects = {}

    categories = requests.get(url).json()
    changed = False
    l = 0
    for category in tqdm(categories.values()):
        if category['code'] in filters: continue
        projects = requests.get(category['api_url']).json()
        for batch in projects['batches'].values():
            batchwise_projects = requests.get(batch['api_url']).json()
            for project in batchwise_projects.values():
                key = project['repo_url'].split('/')[-1]
                if excluded_filename and key in excluded_projects[category['code']]: continue
                if key in all_projects: continue
                if key_only:
                    if category['code'] not in all_projects: all_projects[category['code']] = []
                    all_projects[category['code']].append(key)
                else:
                    all_projects[key] = project
                    data = requests.get(project['api_url']).json()
                    all_projects[key]['team'] = {}
                    if 'team' in data:
                        for member in data['team']:
                            all_projects[key]['team'][member] = {}
                            all_projects[key]['team'][member]['name'] = data['team'][member]['name']
                            all_projects[key]['team'][member]['api_url'] = data['team'][member]['api_url']
                l+=1
                changed = True

    if changed:
        with open(filename, 'w') as f:
            json.dump(all_projects, f)

    print(f"{filename.split('/')[-1]}: {l} projects extracted")

# Run when projects are manually excluded.
def save_excluded_projects(all_projects_filename, extracted_filename, excluded_filename):
    with open(all_projects_filename, 'r') as f:
        all_projects = json.load(f)

    try:
        with open(extracted_filename, 'r') as f:
            extracted_projects = json.load(f)
    except:
        extracted_projects = {}

    try:
        with open(excluded_filename, 'r') as f:
            excluded_projects = json.load(f)
    except:
        excluded_projects = {}

    changed = False
    l = 0
    for category in tqdm(all_projects):
        if category not in excluded_projects: excluded_projects[category] = []
        for project in all_projects[category]:
            excluded = True
            for extracted_project in extracted_projects.values():
                if extracted_project['repo_url'].split('/')[-1] == project:
                    excluded = False
                    break
            if excluded:
                if project not in excluded_projects[category]:
                    excluded_projects[category].append(project)
                    changed = True
                    l+=1

    if changed:
        with open(excluded_filename, 'w') as f:
            json.dump(excluded_projects, f)

    print(f"{excluded_filename.split('/')[-1]}: {l} projects excluded")

def extract_categories(url, filename, projects_filename):
    with open(projects_filename, 'r') as f:
        projects = json.load(f)

    categories = requests.get(url).json()
    categorized_projects = {}
    for category in tqdm(categories):
        _projects = requests.get(categories[category]['api_url']).json()
        title = categories[category]['title'].split('(')[0].strip()
        for batch in _projects['batches']:
            batchwise_projects = requests.get(_projects['batches'][batch]['api_url']).json()
            for project in batchwise_projects.keys():
                if project in projects:
                    if not categorized_projects.get(f'{title} ({category.upper()})'): categorized_projects[f'{title} ({category.upper()})'] = {}
                    if not categorized_projects.get(f'{batch} Batch'): categorized_projects[f'{batch} Batch'] = {}

                    if not categorized_projects[f'{title} ({category.upper()})'].get('count'): categorized_projects[f'{title} ({category.upper()})']['count'] = 0
                    categorized_projects[f'{title} ({category.upper()})']['count'] += 1
                    if not categorized_projects[f'{batch} Batch'].get('count'): categorized_projects[f'{batch} Batch']['count'] = 0
                    categorized_projects[f'{batch} Batch']['count'] += 1

                    categorized_projects[f'{title} ({category.upper()})']['code'] = categories[category]['code']
                    categorized_projects[f'{batch} Batch']['code'] = categories[category]['code']

                    if not categorized_projects[f'{title} ({category.upper()})'].get('projects'): categorized_projects[f'{title} ({category.upper()})']['projects'] = []
                    if not categorized_projects[f'{batch} Batch'].get('projects'): categorized_projects[f'{batch} Batch']['projects'] = []
                    categorized_projects[f'{title} ({category.upper()})']['projects'].append(project)
                    categorized_projects[f'{batch} Batch']['projects'].append(project)

    with open(filename, 'w') as f:
        json.dump(categorized_projects, f)

    print(f"{filename.split('/')[-1]}: {len(categories)} categories extracted")


# Should manually filter out projects that does not relate to embedded systems.
# Categories that are possibly embedded systems related:
# - Undergraduate Research Projects
# - Industrial Automation Projects (CO326)
# - Image Processing Projects (CO543)
if __name__ == '__main__':
    filters = ['co328', '2yp', 'co542', 'co226']
    key_tags = ['embedded', 'embedded-systems', 'robot', 'robotics', 'gpu', 'bio-medical', 'swarm', 'nvidia']
    PATH = '../_data'

    # extract_projects('https://cepdnaclk.github.io/api.ce.pdn.ac.lk/projects/', f'{PATH}/all_projects.json', key_only=True)
    # save_excluded_projects(f'{PATH}/all_projects.json', f'{PATH}/projects.json', f'{PATH}/excluded_projects.json')
    # extract_projects('https://cepdnaclk.github.io/api.ce.pdn.ac.lk/projects/', 
    #                 f'{PATH}/projects.json', 
    #                 f'{PATH}/excluded_projects.json', 
    #                 filters,
    #                 key_tags)
    extract_categories('https://cepdnaclk.github.io/api.ce.pdn.ac.lk/projects/', f'{PATH}/categories.json', f'{PATH}/projects.json')