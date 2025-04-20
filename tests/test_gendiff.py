from gendiff.scripts.generate_diff import (
  converter,
  generate_difference,
  generate_view,
  main,
  sort_output,
)

short_result = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

long_result = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""

first_long_file = {'common': {
    'setting1': 'Value 1', 'setting2': 200, 'setting3': True, 'setting6': {
        'key': 'value', 'doge': {'wow': ''}}}, 'group1': {
            'baz': 'bas', 'foo': 'bar', 'nest': {
                'key': 'value'}}, 'group2': {'abc': 12345, 'deep': {'id': 45}}}

second_long_file = {'common': {
    'follow': False, 'setting1': 'Value 1',
      'setting3': None, 'setting4': 'blah blah', 'setting5': {
          'key5': 'value5'}, 'setting6': {
              'key': 'value', 'ops': 'vops', 'doge': {
                'wow': 'so much'}}}, 'group1': {
                    'foo': 'bar', 'baz': 'bars', 'nest': 'str'},
                      'group3': {'deep': {'id': {'number': 45}}, 'fee': 100500}}

first_short_file = {'host': 'hexlet.io', 'timeout': 50,
                     'proxy': '123.234.53.22', 'follow': False}

second_short_file = {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}

gendiff_short_result = [['   ', 'host:', 'hexlet.io'],
                         ['  +', 'verbose:', 'true'],
                           ['  -', 'timeout:', '50'],
                             ['  +', 'timeout:', '20'],
                               ['  +', 'verbose:', 'true'],
                                 ['  -', 'proxy:', '123.234.53.22'],
                                   ['  +', 'verbose:', 'true'],
                                     ['  -', 'follow:', 'false'],
                                       ['  +', 'verbose:', 'true']]

sort_short_result = [['  -', 'follow:', 'false'],
                      ['   ', 'host:', 'hexlet.io'],
                        ['  -', 'proxy:', '123.234.53.22'],
                          ['  -', 'timeout:', '50'],
                            ['  +', 'timeout:', '20'],
                              ['  +', 'verbose:', 'true']]


def test_main():
    assert main(first_long_file, second_long_file) == long_result

    assert main(first_short_file, second_short_file) == short_result


def test_generate_difference():
    assert generate_difference(first_short_file,
                                second_short_file) == gendiff_short_result


def test_sort_output():
    assert sort_output(gendiff_short_result) == sort_short_result


def test_converter():
    assert converter({"id": {"value": 45}}) == [
        ['   ', 'id:', [['   ', 'value:', '45']]]]


def test_generate_view():
    assert generate_view(sort_short_result) == short_result