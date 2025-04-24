STYLISH_SHORT_RESULT = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

STYLISH_LONG_RESULT = """{
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

PLAIN_LONG_RESULT = """Property 'common.follow' was added with value: false
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

PLAIN_SHORT_RESULT = """Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From '50' to '20'
Property 'verbose' was added with value: true"""

FIRST_LONG_FILE = {'common': {
    'setting1': 'Value 1', 'setting2': 200, 'setting3': True, 'setting6': {
        'key': 'value', 'doge': {'wow': ''}}}, 'group1': {
            'baz': 'bas', 'foo': 'bar', 'nest': {
                'key': 'value'}}, 'group2': {'abc': 12345, 'deep': {'id': 45}}}

SECOND_LONG_FILE = {'common': {
    'follow': False, 'setting1': 'Value 1',
      'setting3': None, 'setting4': 'blah blah', 'setting5': {
          'key5': 'value5'}, 'setting6': {
              'key': 'value', 'ops': 'vops', 'doge': {
                'wow': 'so much'}}}, 'group1': {
                    'foo': 'bar', 'baz': 'bars', 'nest': 'str'},
                      'group3': {'deep': {'id': {'number': 45}}, 'fee': 100500}}

FIRST_SHORT_FILE = {'host': 'hexlet.io', 'timeout': 50,
                     'proxy': '123.234.53.22', 'follow': False}

SECOND_SHORT_FILE = {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}

GENDIFF_SHORT_RESULT = [['   ', 'host:', 'hexlet.io'],
                         ['  +', 'verbose:', 'true'],
                           ['  -', 'timeout:', '50'],
                             ['  +', 'timeout:', '20'],
                               ['  +', 'verbose:', 'true'],
                                 ['  -', 'proxy:', '123.234.53.22'],
                                   ['  +', 'verbose:', 'true'],
                                     ['  -', 'follow:', 'false'],
                                       ['  +', 'verbose:', 'true']]

GENDIFF_LONG_RESULT = [['   ', 'common:', [['   ', 'setting1:', 'Value 1'],
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

SHORT_SORTED_OUTPUT = [['  -', 'follow:', 'false'],
                      ['   ', 'host:', 'hexlet.io'],
                        ['  -', 'proxy:', '123.234.53.22'],
                          ['  -', 'timeout:', '50'],
                            ['  +', 'timeout:', '20'],
                              ['  +', 'verbose:', 'true']]

LONG_SORTED_OUTPUT = [['   ', 'common:', [['  +', 'follow:', 'false'],
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

LONG_JSON_OUTPUT = {'common': {'follow': 0, 'setting3': None, 'setting4':
 'blah blah', 'setting5': {'key5': 'value5'}, 'setting6': {'doge': {'wow':
  'so much'}, 'ops': 'vops'}}, 'group1': {'baz': 'bars', 'nest': 'str'},
    'group3': {'deep': {'id': {'number': 45}}, 'fee': 100500}}

SHORT_JSON_OUTPUT = {'timeout': 20, 'verbose': 1}