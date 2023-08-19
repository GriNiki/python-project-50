import json
import yaml
import os
from yaml.loader import BaseLoader


def parser(path):
    with open(path, 'r') as file:
        if '.json' in os.path.split(path)[1]:
            return json.load(file)
        elif '.yaml' or '.yml' in os.path.split(path)[1]:
            return yaml.load(file, Loader=BaseLoader)
