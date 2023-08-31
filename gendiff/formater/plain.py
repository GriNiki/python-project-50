def format_item(item):

    if isinstance(item, dict):
        formatted_item = '[complex value]'

    elif isinstance(item, bool):
        formatted_item = str(item).lower()

    elif item is None:
        formatted_item = 'null'

    elif isinstance(item, (int, float)):
        formatted_item = str(item)

    else:
        formatted_item = f"'{item}'"

    return formatted_item


# flake8: noqa: C901
def plain(diff):

    def walk(node, path):
        result = []

        for item in node:
            item_path = f"{path}{item['value']}"

            if item['status'] == 'added':
                string = (f"Property '{item_path}'"
                          f" was added with value:"
                          f" {format_item(item['item'])}")
                result.append(string)

            elif item['status'] == 'plain_changes':
                string = (f"Property '{item_path}' was updated."
                          f" From {format_item(item['old_value'])}"
                          f" to {format_item(item['new_value'])}")
                result.append(string)

            elif item['status'] == 'delete':
                string = f"Property '{item_path}' was removed"
                result.append(string)

            elif item['status'] == 'attachment':
                string = walk(item['children'], item_path + '.')
                result.append(string)

        return '\n'.join(result)

    return walk(diff, '')
