import json

def read_api_key(key_path, key_name):
    with open(key_path) as f:
        data = json.load(f)
        api_key = data.get(key_name)
        return api_key
