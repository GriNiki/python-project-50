import json
import yaml
import os


def parser(path):
    with open(path, 'r') as file:
        if '.json' in os.path.split(path)[1]:
            return json.load(file)
        elif '.yaml' or '.yml' in os.path.split(path)[1]:
            return yaml.safe_load(file)
