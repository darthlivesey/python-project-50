from gendiff.scripts.generate_diff import generate_difference
from gendiff.scripts.parser import parse_files


def test_generate_difference():
    first_file, second_file = parse_files("tests/test_data/file1.json",
                                    "tests/test_data/file2.json")
    assert str(generate_difference(first_file, second_file)) == """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

    first_file, second_file = parse_files("tests/test_data/file1.yaml",
                                    "tests/test_data/file2.yaml")
    assert str(generate_difference(first_file, second_file)) == """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

    first_file, second_file = parse_files("tests/test_data/file1.yaml",
                                    "tests/test_data/file2.json")
    assert str(generate_difference(first_file, second_file)) == """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

    first_file, second_file = parse_files("tests/test_data/file1.json",
                                    "tests/test_data/file2.yaml")
    assert str(generate_difference(first_file, second_file)) == """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
