from gendiff.parser import parser
from gendiff.formater.format import make_format
from gendiff.generate_diff_tree import generate_diff_tree
from gendiff.file_opener import open_file, make_extension


def generate_diff(file1_path, file2_path, format='stylish'):
    file1 = parser(open_file(file1_path), make_extension(file1_path))
    file2 = parser(open_file(file2_path), make_extension(file2_path))
    diff = generate_diff_tree(file1, file2)
    format_diff = make_format(diff, format)
    return format_diff
