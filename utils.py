import json
import os

#Load keys and secrets from json file
def load_keys(path):
    if not os.path.exists(path):
        raise Exception("Path to load json with keys not found")
    return json.loads(open(path, 'r').read())

