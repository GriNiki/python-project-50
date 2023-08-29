from gendiff.generate_diff import generate_diff


FILES = {
    'file1_json': 'testes/fixture/test_file1.json',
    'file2_json': 'testes/fixture/test_file2.json',

    'file1_yaml': 'testes/fixture/test_file1.yaml',
    'file2_yaml': 'testes/fixture/test_file2.yaml',

    'file1_tree_json': 'testes/fixture/file1_tree.json',
    'file2_tree_json': 'testes/fixture/file2_tree.json',

    'file1_tree_yaml': 'testes/fixture/file1_tree.yaml',
    'file2_tree_yaml': 'testes/fixture/file2_tree.yaml',

    'expected_result_json_flat': 'testes/fixture/test_json_result.txt',
    'expected_result_yaml_flat': 'testes/fixture/test_yaml_result.txt',
    'expected_result_tree': 'testes/fixture/test_tree_result.txt',
    'expected_result_plain': 'testes/fixture/test_style_plain.txt',
    'expected_result_json': 'testes/fixture/test_style_json.txt',
}


def test_flat_json_file():
    with open(FILES['expected_result_json_flat'], 'r') as file:
        expected = file.read()
    assert generate_diff(FILES['file1_json'], FILES['file2_json']) == expected


def test_flat_yaml_file():
    with open(FILES['expected_result_yaml_flat'], 'r') as file:
        expected = file.read()
    assert generate_diff(FILES['file1_yaml'], FILES['file2_yaml']) == expected


def test_stylish_format():
    with open(FILES['expected_result_tree'], 'r') as file:
        expected = file.read()
    assert generate_diff(FILES['file1_tree_json'], FILES['file2_tree_json'], 'stylish') == expected
    assert generate_diff(FILES['file1_tree_yaml'], FILES['file2_tree_yaml'], 'stylish') == expected


def test_plain_format():
    with open(FILES['expected_result_plain'], 'r') as file:
        expected = file.read()
    assert generate_diff(FILES['file1_tree_json'], FILES['file2_tree_json'], 'plain') == expected
    assert generate_diff(FILES['file1_tree_yaml'], FILES['file2_tree_yaml'], 'plain') == expected


def test_json_format():
    with open(FILES['expected_result_json'], 'r') as file:
        expected = file.read()
    assert generate_diff(FILES['file1_tree_json'], FILES['file2_tree_json'], 'json') == expected
    assert generate_diff(FILES['file1_tree_yaml'], FILES['file2_tree_yaml'], 'json') == expected
