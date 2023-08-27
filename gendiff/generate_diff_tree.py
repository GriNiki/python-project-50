def generate_diff_tree(dict1, dict2):

    diff_tree = []
    sorted_key = sorted(set(dict1) | set(dict2))

    for key in sorted_key:

        if key not in dict1:
            diff_tree.append({
                'value': key,
                'item': dict2[key],
                'status': 'added'
                                })

        elif key not in dict2:
            diff_tree.append({
                    'value': key,
                    'item': dict1[key],
                    'status': 'delete'
                                })

        elif dict1[key] == dict2[key]:
            diff_tree.append({
                'value': key,
                'item': dict1[key],
                'status': 'no_change'
                                })

        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            diff_tree.append({
                    'value': key,
                    'children': generate_diff_tree(dict1[key], dict2[key]),
                    'status': 'attachment'
                                })
        else:
            diff_tree.append({
                    'name': key,
                    'old_value': dict1[key],
                    'new_value': dict2[key],
                    'status': 'plain_changes'
                                })
    return diff_tree
