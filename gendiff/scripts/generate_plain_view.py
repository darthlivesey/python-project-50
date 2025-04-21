def format_input(input):
    for element in input:
        if element[2] not in [
            "null", "false", "true"] and type(element[2]) is not list:
            element[2] = f"'{element[2]}'"

    return input


def generate_plain_view(input, prefix=""):
    flag = False
    result_string = ""
    for element in format_input(input):
        if element[0] == "   " or flag:
            if type(element[2]) is str or flag:
                flag = False
                continue
            else:
                result_string += generate_plain_view(
                    element[2], prefix + f"{element[1][:-1]}.") + "\n"
        else:
            elements_with_the_same_key = [
                i for i in input if i[1] == element[1]]
            if len(elements_with_the_same_key) == 1:
                if element[0] == "  +" and type(element[2]) is not list:
                    result_string += ("Property '" + prefix + element[1][:-1]
                                       + "' was added with value: "
                                         + element[2] + "\n")
                elif element[0] == "  +" and type(element[2]) is list:
                    result_string += ("Property '" + prefix + element[1][:-1]
                                       + "' was added with value: "
                                       "[complex value]\n")
                else:
                    result_string += ("Property '" + prefix + element[1][:-1]
                                       + "' was removed\n")
            else:
                if type(elements_with_the_same_key[0][2]) is str and type(
                    elements_with_the_same_key[1][2]) is not str:
                    result_string += ("Property '" + prefix + element[1][:-1]
                                       + "' was updated. From "
                                         + elements_with_the_same_key[0][2]
                                           + " to [complex value]\n")
                elif type(elements_with_the_same_key[0][2]) is not str and type(
                    elements_with_the_same_key[1][2]) is str:
                    result_string += ("Property '" + prefix + element[1][:-1]
                                       + "' was updated. "
                                       "From [complex value] to "
                                         + elements_with_the_same_key[1][2]
                                           + "\n")
                elif (type(elements_with_the_same_key[0][2]) is type(
                    elements_with_the_same_key[1][2])) and type(
                        elements_with_the_same_key[0][2]) is str:
                    result_string += ("Property '" + prefix + element[1][:-1]
                                       + "' was updated. From "
                                         + elements_with_the_same_key[0][2]
                                           + " to "
                                             + elements_with_the_same_key[1][2]
                                               + "\n")
                else:
                    result_string += generate_plain_view(
                        elements_with_the_same_key, prefix
                          + f"{element[1][:-1]}.") + "\n"
                flag = True

    return result_string[:-1]