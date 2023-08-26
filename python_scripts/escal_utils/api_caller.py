import requests

class APICaller:
    def __init__(self, base_url):
        self.base_url = base_url

    def request(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

            