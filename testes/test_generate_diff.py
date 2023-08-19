from gendiff.generate_diff import generate_diff


def test_generate_diff():
    file1_json = 'testes/fixture/test_file1.json'
    file2_json = 'testes/fixture/test_file2.json'
    file1_yaml = 'testes/fixture/test_file1.yaml'
    file2_yaml = 'testes/fixture/test_file2.yaml'
    expected_result_json = open('testes/fixture/test_json_result.txt').read()
    expected_result_yaml = open('testes/fixture/test_yaml_result.txt').read()

    assert generate_diff(file1_json, file2_json) == expected_result_json
    assert generate_diff(file1_yaml, file2_yaml) == expected_result_yaml
