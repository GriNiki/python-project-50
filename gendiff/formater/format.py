from gendiff.formater.stylish import stylish
from gendiff.formater.plain import plain
from gendiff.formater.json import make_json_format


def make_format(diff, format):

    if format == 'stylish':
        return stylish(diff)

    elif format == 'plain':
        return plain(diff)

    elif format == 'json':
        return make_json_format(diff)
