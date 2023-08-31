import json
import yaml


def parser(file, extension):

    if '.json' in extension:
        return json.load(file)

    elif '.yaml' or '.yml' in extension:
        return yaml.safe_load(file)
