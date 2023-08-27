from gendiff.formater.stylish import stylish


def make_format(diff, format):
    if format == 'stylish':
        return stylish(diff)
