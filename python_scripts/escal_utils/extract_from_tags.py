class ExtaractFromTags:
    def __init__(self, api_caller, tags):
        self.api_caller = api_caller
        self.tags = tags

    def extract(self, endpoint, params=None):
        response = self.api_caller.request(endpoint, params)
        results = []

        for i in self.tags:
            for j in response[i]:
                if j not in results: results.append(j)

        return results