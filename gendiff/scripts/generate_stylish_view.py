def generate_stylish_view(input, deep=0):
    result_string = "{\n"
    for element in input:
        if type(element[2]) is str:
            result_string += deep * "    " + " ".join(
                [i.strip("'") for i in element]) + "\n"
        else:
            result_string += deep * "    " + (
                f"{element[0]} {element[1]} " 
                f"{generate_stylish_view(element[2], (deep + 1))}") + "\n"

    return result_string + deep * "    " + "}"
