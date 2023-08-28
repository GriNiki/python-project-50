from gendiff.generate_diff import generate_diff


def test_generate_diff():
    file1_json = 'testes/fixture/test_file1.json'
    file2_json = 'testes/fixture/test_file2.json'
    file1_yaml = 'testes/fixture/test_file1.yaml'
    file2_yaml = 'testes/fixture/test_file2.yaml'
    file1_tree_json = 'testes/fixture/file1_tree.json'
    file2_tree_json = 'testes/fixture/file2_tree.json'
    file1_tree_yaml = 'testes/fixture/file1_tree.yaml'
    file2_tree_yaml = 'testes/fixture/file2_tree.yaml'

    expected_result = open('testes/fixture/test_json_result.txt', 'r').read()
    expected_result_tree = open('testes/fixture/test_tree_result.txt', 'r').read()
    expected_result_plain = open('testes/fixture/test_style_plain.txt', 'r').read()

    assert generate_diff(file1_json, file2_json) == expected_result
    assert generate_diff(file1_yaml, file2_yaml) == expected_result
    assert generate_diff(file1_tree_json, file2_tree_json) == expected_result_tree
    assert generate_diff(file1_tree_yaml, file2_tree_yaml) == expected_result_tree
    assert generate_diff(file1_tree_json, file2_tree_json, 'plain') == expected_result_plain