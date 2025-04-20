def main(first_file, second_file):
    return generate_view(sort_output(generate_difference(
        first_file, second_file, format_name="stylish")))


def generate_difference(first_file: dict,
                         second_file: dict, format_name="stylish"):
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


def generate_view(input, deep=0):
    result_string = "{\n"
    for element in input:
        if type(element[2]) is str:
            result_string += deep * "    " + " ".join(element) + "\n"
        else:
            result_string += deep * "    " + (
                f"{element[0]} {element[1]} " 
                f"{generate_view(element[2], (deep + 1))}") + "\n"

    return result_string + deep * "    " + "}"
