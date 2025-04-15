from gendiff.scripts.generate_diff import generate_difference


def test_generate_difference():
    assert str(generate_difference("tests/test_data/file1.json",
                                    "tests/test_data/file2.json")) == """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""