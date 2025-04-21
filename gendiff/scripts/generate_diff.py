from gendiff.scripts.generate_plain_view import generate_plain_view
from gendiff.scripts.generate_stylish_view import generate_stylish_view


def main(first_file, second_file, format_name):
    sorted_output = sort_output(generate_difference(
        first_file, second_file))
    if format_name == "stylish":
        return generate_stylish_view(sorted_output)
    elif format_name == "plain":
        return generate_plain_view(sorted_output)


def generate_difference(first_file: dict, second_file: dict):
    output = []

    for key in first_file.keys():
        if key in second_file.keys():
            if (type(first_file[key]) is type(
                second_file[key])) and type(first_file[key]) is not dict:
                if first_file[key] == second_file[key]:
                    output.append(
                        ["   ", key + ":", converter(first_file[key])])
                else:
                    output.append(
                        ["  -", key + ":", converter(first_file[key])])
                    output.append(
                        ["  +", key + ":", converter(second_file[key])])
            elif (type(first_file[key]) is not type(
                second_file[key])) and type(first_file[key]) is dict:
                output.append(
                    ["  -", key + ":", converter(first_file[key])])
                output.append(
                    ["  +", key + ":", converter(second_file[key])])
            elif (type(first_file[key]) is not type(
                second_file[key])) and type(first_file[key]) is not dict:
                output.append(
                    ["  -", key + ":", converter(first_file[key])])
                output.append(
                    ["  +", key + ":", converter(second_file[key])])
            else:
                output.append(
                    ["   ", key + ":", generate_difference(
                        first_file[key], second_file[key])])
        else:
            output.append(
                ["  -", key + ":", converter(first_file[key])])

        for key in second_file.keys():
            if key not in first_file.keys():
                output.append(
                    ["  +", key + ":", converter(second_file[key])])

    return output


def converter(content):
    output = []
    if content is None:
        return "null"
    elif type(content) is bool:
        return str(content).lower()
    elif type(content) is not dict:
        return str(content)
    else:
        for key in content.keys():
            if type(content[key]) is dict:
                output.append(
                    ["   ", key + ":", converter(content[key])])
            else:
                output.append(
                    ["   ", key + ":", str(content[key]).lower()])

    return output


def sort_output(input):
    unique_list = []
    for element in input:
        if element not in unique_list: 
            if type(element[2]) is dict:
                element[2] = [i for i in element[2]]
                element[2] = sort_output(element[2])
            if type(element[2]) is list:
                element[2] = sort_output(element[2])
            unique_list.append(element)

    unique_list.sort(key=lambda element: element[0], reverse=True)
    unique_list.sort(key=lambda element: element[1])
    return unique_list


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
