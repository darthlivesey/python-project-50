stylish_short_result = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

stylish_long_result = """{
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

plain_long_result = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""

plain_short_result = """Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From '50' to '20'
Property 'verbose' was added with value: true"""

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

gendiff_long_result = [['   ', 'common:', [['   ', 'setting1:', 'Value 1'],
 ['  +', 'follow:', 'false'], ['  +', 'setting4:', 'blah blah'], ['  +',
  'setting5:', [['   ', 'key5:', 'value5']]], ['  -', 'setting2:', '200'],
   ['  +', 'follow:', 'false'], ['  +', 'setting4:', 'blah blah'], ['  +',
    'setting5:', [['   ', 'key5:', 'value5']]], ['  -', 'setting3:', 'true'],
     ['  +', 'setting3:', 'null'], ['  +', 'follow:', 'false'], ['  +',
      'setting4:', 'blah blah'], ['  +', 'setting5:', [['   ', 'key5:',
       'value5']]], ['   ', 'setting6:', [['   ', 'key:', 'value'], ['  +',
        'ops:', 'vops'], ['   ', 'doge:', [['  -', 'wow:', ''], ['  +', 'wow:',
         'so much']]], ['  +', 'ops:', 'vops']]], ['  +', 'follow:', 'false'],
          ['  +', 'setting4:', 'blah blah'], ['  +', 'setting5:', [['   ',
           'key5:', 'value5']]]]], ['  +', 'group3:', [['   ', 'deep:', [['   ',
            'id:', [['   ', 'number:', '45']]]]], ['   ', 'fee:', '100500']]],
             ['   ', 'group1:', [['  -', 'baz:', 'bas'],
              ['  +', 'baz:', 'bars'], ['   ', 'foo:', 'bar'], ['  -', 'nest:',
               [['   ', 'key:', 'value']]], ['  +', 'nest:', 'str']]], ['  +',
                'group3:', [['   ', 'deep:', [['   ', 'id:', [['   ', 'number:',
                 '45']]]]], ['   ', 'fee:', '100500']]], ['  -', 'group2:',
                  [['   ', 'abc:', '12345'], ['   ', 'deep:', [['   ', 'id:',
                   '45']]]]], ['  +', 'group3:', [['   ', 'deep:', [['   ',
                    'id:', [['   ', 'number:', '45']]]]], ['   ', 'fee:',
                     '100500']]]]

short_sorted_output = [['  -', 'follow:', 'false'],
                      ['   ', 'host:', 'hexlet.io'],
                        ['  -', 'proxy:', '123.234.53.22'],
                          ['  -', 'timeout:', '50'],
                            ['  +', 'timeout:', '20'],
                              ['  +', 'verbose:', 'true']]

long_sorted_output = [['   ', 'common:', [['  +', 'follow:', 'false'],
 ['   ', 'setting1:', 'Value 1'], ['  -', 'setting2:', '200'], ['  -',
  'setting3:', 'true'], ['  +', 'setting3:', 'null'], ['  +',
   'setting4:', 'blah blah'], ['  +', 'setting5:', [['   ', 'key5:',
    'value5']]], ['   ', 'setting6:', [['   ', 'doge:', [['  -',
     'wow:', ''], ['  +', 'wow:', 'so much']]], ['   ', 'key:',
      'value'], ['  +', 'ops:', 'vops']]]]], ['   ', 'group1:',
       [['  -', 'baz:', 'bas'], ['  +', 'baz:', 'bars'], ['   ',
        'foo:', 'bar'], ['  -', 'nest:', [['   ', 'key:', 'value']]],
         ['  +', 'nest:', 'str']]], ['  -', 'group2:', [['   ', 'abc:',
          '12345'], ['   ', 'deep:', [['   ', 'id:', '45']]]]], ['  +',
           'group3:', [['   ', 'deep:', [['   ', 'id:', [['   ',
            'number:', '45']]]]], ['   ', 'fee:', '100500']]]]