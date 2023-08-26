from escal_utils.api_caller import APICaller
from escal_utils.extract_from_tags import ExtaractFromTags
import json

api_url = "https://api.ce.pdn.ac.lk/"
tags = ["GPU",
    "GPU acceleration"]

endpoint = "publications/v1/filter/tags/"
filename = "../_data/gpu_pubs.json"

if __name__ == "__main__":
    api =  APICaller(api_url)
    pub_extractor = ExtaractFromTags(api, tags)
    pubs = pub_extractor.extract(endpoint=endpoint)

    with open(filename, "w") as file:
        json.dump(pubs, file, indent=4)
