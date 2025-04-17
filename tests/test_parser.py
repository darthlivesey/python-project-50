from gendiff.scripts.parser import parse_files

first_file = {'host': 'hexlet.io', 'timeout': 50,
              'proxy': '123.234.53.22', 'follow': False}
second_file = {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}


def test_parse_files():
    assert parse_files("tests/test_data/file1.json",
    "tests/test_data/file2.json") == (first_file, second_file)

    assert parse_files("tests/test_data/file1.yaml",
    "tests/test_data/file2.yaml") == (first_file, second_file)

    assert parse_files("tests/test_data/file1.yaml",
    "tests/test_data/file2.json") == (first_file, second_file)

    assert parse_files("tests/test_data/file1.json",
    "tests/test_data/file2.yaml") == (first_file, second_file)