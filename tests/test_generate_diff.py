from gendiff.generate_diff import generate_diff


FILES = {
    'file1_json': 'tests/fixture/json/test_file1.json',
    'file2_json': 'tests/fixture/json/test_file2.json',

    'file1_yaml': 'tests/fixture/yaml/test_file1.yaml',
    'file2_yaml': 'tests/fixture/yaml/test_file2.yaml',

    'file1_tree_json': 'tests/fixture/json/file1_tree.json',
    'file2_tree_json': 'tests/fixture/json/file2_tree.json',

    'file1_tree_yaml': 'tests/fixture/yaml/file1_tree.yaml',
    'file2_tree_yaml': 'tests/fixture/yaml/file2_tree.yaml',

    'expected_result_json_flat': 'tests/fixture/expected/test_json_result.txt',
    'expected_result_yaml_flat': 'tests/fixture/expected/test_yaml_result.txt',
    'expected_result_tree': 'tests/fixture/expected/test_tree_result.txt',
    'expected_result_plain': 'tests/fixture/expected/test_style_plain.txt',
    'expected_result_json': 'tests/fixture/expected/test_style_json.txt',
}


def open_file(path):
    with open(path, 'r') as file:
        return file.read()


def test_flat_json_file():
    assert generate_diff(FILES['file1_json'], FILES['file2_json']) == open_file(FILES['expected_result_json_flat'])


def test_flat_yaml_file():
    assert generate_diff(FILES['file1_yaml'], FILES['file2_yaml']) == open_file(FILES['expected_result_yaml_flat'])


def test_stylish_format():
    assert generate_diff(FILES['file1_tree_json'], FILES['file2_tree_json'], 'stylish') == open_file(FILES['expected_result_tree'])
    assert generate_diff(FILES['file1_tree_yaml'], FILES['file2_tree_yaml'], 'stylish') == open_file(FILES['expected_result_tree'])


def test_plain_format():
    assert generate_diff(FILES['file1_tree_json'], FILES['file2_tree_json'], 'plain') == open_file(FILES['expected_result_plain'])
    assert generate_diff(FILES['file1_tree_yaml'], FILES['file2_tree_yaml'], 'plain') == open_file(FILES['expected_result_plain'])


def test_json_format():
    assert generate_diff(FILES['file1_tree_json'], FILES['file2_tree_json'], 'json') == open_file(FILES['expected_result_json'])
    assert generate_diff(FILES['file1_tree_yaml'], FILES['file2_tree_yaml'], 'json') == open_file(FILES['expected_result_json'])
