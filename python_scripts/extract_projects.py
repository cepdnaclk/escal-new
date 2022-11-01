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

    org_repos = {}
    if not key_only:
        org_url = 'https://api.github.com/orgs/cepdnaclk/repos?page='
        page = 1
        print('Extracting organization repos...')
        repos = requests.get(org_url + str(page)).json()
        while repos:
            for repo in repos:
                org_repos[repo['name']] = {}
                org_repos[repo['name']]['stars'] = repo['stargazers_count']
                org_repos[repo['name']]['updated_at'] = repo['updated_at']
            page += 1
            repos = requests.get(org_url + str(page)).json()

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
                if key_only:
                    if category['code'] not in all_projects: all_projects[category['code']] = []
                    if key not in all_projects[category['code']]: all_projects[category['code']].append(key)
                elif key in org_repos:
                    all_projects[key] = project
                    data = requests.get(project['api_url']).json()
                    all_projects[key]['stars'] = org_repos[key]['stars']
                    all_projects[key]['updated_at'] = org_repos[key]['updated_at']
                    all_projects[key]['team'] = {}
                    if 'team' in data:
                        for member in data['team']:
                            all_projects[key]['team'][member] = {}
                            all_projects[key]['team'][member]['name'] = data['team'][member]['name']
                            all_projects[key]['team'][member]['api_url'] = data['team'][member]['api_url']
                l+=1
                changed = True

    if changed:
        sorted_projects = all_projects
        if not key_only:
            for k, v in sorted(all_projects.items(), key=lambda d: d[1]['updated_at'], reverse=True):
                sorted_projects[k] = v

        with open(filename, 'w') as f:
            json.dump(sorted_projects, f)

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

# Use to extract categorized project data.
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
            cat_key = f'{title} ({category.upper()})'
            batch_key = f'{batch} Batch Projects'
            for project in batchwise_projects.keys():
                if project in projects:
                    if not categorized_projects.get(cat_key): categorized_projects[cat_key] = {}
                    if not categorized_projects.get(batch_key): categorized_projects[batch_key] = {}

                    if not categorized_projects[cat_key].get('count'): categorized_projects[cat_key]['count'] = 0
                    categorized_projects[cat_key]['count'] += 1
                    if not categorized_projects[batch_key].get('count'): categorized_projects[batch_key]['count'] = 0
                    categorized_projects[batch_key]['count'] += 1

                    categorized_projects[cat_key]['code'] = categories[category]['code']
                    categorized_projects[batch_key]['code'] = batch.lower()

                    if not categorized_projects[cat_key].get('projects'): categorized_projects[cat_key]['projects'] = []
                    if not categorized_projects[batch_key].get('projects'): categorized_projects[batch_key]['projects'] = []
                    categorized_projects[cat_key]['projects'].append(project)
                    categorized_projects[batch_key]['projects'].append(project)

                    categorized_projects[cat_key]['parent'] = '/projects'
                    categorized_projects[batch_key]['parent'] = '/projects'

    sorted_projects = {}
    for k in sorted(categorized_projects, key=len, reverse=True):
        sorted_projects[k] = categorized_projects[k]

    with open(filename, 'w') as f:
        json.dump(sorted_projects, f)

    print(f"{filename.split('/')[-1]}: {len(categories)} categories extracted")


# Should manually filter out projects that does not relate to embedded systems.
# Categories that are possibly embedded systems related:
# - Undergraduate Research Projects
# - Industrial Automation Projects (CO326)
# - Image Processing Projects (CO543)
if __name__ == '__main__':
    filters = ['co328', '2yp', 'co542', 'co226', 'co227']
    key_tags = ['embedded', '3yp', 'embedded-systems', 'embedded-system', 'iot', 'arduino', 'fpga', 'raspberry', 'robot', 'robotics', 'gpu', 'bio-medical', 'swarm', 'nvidia']
    PATH = '../_data'

    # extract_projects('https://api.ce.pdn.ac.lk/projects/v1/', f'{PATH}/all_projects.json', key_only=True)
    # extract_projects('https://api.ce.pdn.ac.lk/projects/v1/', 
    #                 f'{PATH}/projects.json', 
    #                 f'{PATH}/excluded_projects.json', 
    #                 filters,
    #                 key_tags)
    # save_excluded_projects(f'{PATH}/all_projects.json', f'{PATH}/projects.json', f'{PATH}/excluded_projects.json')
    # extract_categories('https://api.ce.pdn.ac.lk/projects/v1/', f'{PATH}/project_categories.json', f'{PATH}/projects.json')