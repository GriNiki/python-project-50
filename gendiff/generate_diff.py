import json
from gendiff.parser import parser


def generate_diff(file1_path, file2_path):
    file1_dict = parser(file1_path)
    file2_dict = parser(file2_path)
    diff = dict()
    sorted_list_key = sorted(
        list(
            set(file1_dict.keys()) | set(file2_dict.keys()
                                         )))
    for key in sorted_list_key:
        if file1_dict.get(key) == file2_dict.get(key):
            diff[key] = file1_dict[key]
        elif file1_dict.get(key) and file2_dict.get(key):
            diff[f'-{key}'] = file1_dict[key]
            diff[f'+{key}'] = file2_dict[key]
        elif file1_dict.get(key) is not None:
            diff[f'-{key}'] = file1_dict[key]
        elif file2_dict.get(key) is not None:
            diff[f'+{key}'] = file2_dict[key]
    return json.dumps(diff, indent=2)
