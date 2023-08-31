import os


def open_file(path):
    return open(path)


def make_extension(path):
    return os.path.split(path)[1]
