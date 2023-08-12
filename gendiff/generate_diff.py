import json


def generate_diff(file1_path, file2_path):
    with (
        open(file1_path, 'r') as json_file1,
        open(file2_path, 'r') as json_file2,
    ):
        diff = dict()
        file1_dict = json.load(json_file1)
        file2_dict = json.load(json_file2)
        sorted_list_key = sorted(list(set(file1_dict.keys()) | set(file2_dict.keys())))
        for key in sorted_list_key:
            if file1_dict.get(key) == file2_dict.get(key):
                diff[key] = file1_dict[key]
            elif file1_dict.get(key) and file2_dict.get(key):
                diff[f'-{key}'] = file1_dict[key]
                diff[f'+{key}'] = file2_dict[key]
            elif file1_dict.get(key) != None:
                diff[f'-{key}'] = file1_dict[key]
            elif file2_dict.get(key) != None:
                diff[f'+{key}'] = file2_dict[key]
        return json.dumps(diff, indent=2)
