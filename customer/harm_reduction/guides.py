import json

def get_guide(substance):
    with open('customer/harm_reduction/data/guides.json') as f:
        guides = json.load(f)
    return guides.get(substance, "Guide not found.")
