from gendiff.formater.stylish import stylish
from gendiff.formater.plain import plain


def make_format(diff, format):
    if format == 'stylish':
        return stylish(diff)

    elif format == 'plain':
        return plain(diff)
