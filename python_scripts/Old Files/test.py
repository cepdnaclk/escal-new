import requests
import json
repo_url = "https://github.com/cepdnaclk/e17-3yp-smart-shopping-cart"
# Split the URL by "https://github.com/cepdnaclk/"
parts = repo_url.split("https://github.com/cepdnaclk/")

# Check if the URL matches the expected format
if len(parts) == 2:
    # The second part contains what you want
    desired_part = parts[1]
    print(desired_part)
else:
    print("URL format is not as expected.")
desired_part = 'e17-3yp-smart-shopping-cart'
github_url = "https://api.github.com/repos/cepdnaclk/"+desired_part

response = requests.get(github_url)
if response.status_code == 200:
    projects_data = response.json()

    print(projects_data['stargazers_count'])
    print(projects_data['updated_at'])