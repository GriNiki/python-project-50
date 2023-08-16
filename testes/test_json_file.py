from gendiff.generate_diff import generate_diff


def test_generate_diff():
    file1_json = 'fixture/test_file1.json'
    file2_json = 'fixture/test_file2.json'
    expected_result_json = open('fixture/test_json_result.txt').read()

    assert generate_diff(file1_json, file2_json) == expected_result_json
