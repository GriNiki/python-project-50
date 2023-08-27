import itertools


def stylish(items, depth=0):
    result = []
    indent = (' ' * 4) * depth

    for item in items:
        if item['status'] == 'no_change':
            result.append(make_line(item['value'], item['item'], ' ', depth))

        elif item['status'] == 'added':
            result.append(make_line(item['value'], item['item'], '+', depth))

        elif item['status'] == 'delete':
            result.append(make_line(item['value'], item['item'], '-', depth))

        elif item['status'] == 'attachment':
            result.append(f"{indent}    {item['value']}:"
                          f" {stylish(item['children'], depth+1)}")

        elif item['status'] == 'plain_changes':
            result.append(make_line(item['name'], item['old_value'],
                                    '-', depth))
            result.append(make_line(item['name'], item['new_value'],
                                    '+', depth))

    return '\n'.join(itertools.chain("{", result, [indent + "}"]))


def make_line(key, value, symbol, depth):
    indent = (' ' * 4) * depth
    line = []

    if isinstance(value, dict):
        dict_lines = []

        for k, v in sorted(value.items()):
            dict_lines.append(make_line(k, v, ' ',
                                        depth + 1))

        result_line = '\n'.join(itertools.chain('{',
                                dict_lines, [indent + '    }']))
        line.append(f"{indent}  {symbol} {key}: {result_line}")

    else:
        line.append(f'{indent}  {symbol} {key}: {format_item(value)}')

    return '\n'.join(line)


def format_item(item):
    if isinstance(item, bool):
        formatted_item = str(item).lower()

    elif item is None:
        formatted_item = 'null'

    elif isinstance(item, (int, float)):
        formatted_item = str(item)

    elif item == '':
        formatted_item = ''

    else:
        formatted_item = f'{item}'

    return formatted_item
