import pytest
from gendiff.scripts.gendiff import main


FILES = {
    'file1_json': 'tests/fixture/json/test_file1.json',
    'file2_json': 'tests/fixture/json/test_file2.json'
}


@pytest.mark.parametrize("option", ("-h", "--help"))
def test_run_help(capsys, option):

    try:
        main([option])
    except SystemExit:
        pass

    output = capsys.readouterr().out
    assert "Compares two configuration files and shows a difference." in output


def test_work_default():
    main([FILES['file1_json'], FILES['file2_json']])


@pytest.mark.parametrize("option", ("-f", "--format"))
def test_work_style(option):
    main([option, "plain", FILES['file1_json'], FILES['file2_json']])


def test_error(capsys):

    with pytest.raises(SystemExit):
        main(["file1"])

    captured = capsys.readouterr()
    assert "the following arguments are required: second_file\n" in captured.err


def test_error_empty_call(capsys):
    with pytest.raises(SystemExit):
        main([])

    captured = capsys.readouterr()
    assert "the following arguments are required: first_file, second_file\n" in captured.err
