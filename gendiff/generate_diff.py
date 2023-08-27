from gendiff.parser import parser
from gendiff.formater.format import make_format
from gendiff.generate_diff_tree import generate_diff_tree


def generate_diff(file1_path, file2_path, format='stylish'):
    file1 = parser(file1_path)
    file2 = parser(file2_path)
    diff = generate_diff_tree(file1, file2)
    format_diff = make_format(diff, format)
    return format_diff
