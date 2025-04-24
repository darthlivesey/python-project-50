def generate_json_view(input, flag=False):
    output = {}
    for element in input:
        temp = element[2]
        if type(element[2]) is not list:
            if element[2] == "null":
                temp = None
            elif element[2] == "true":
                temp = True
            elif element[2] == "false":
                temp = False
            else:
                try:
                    temp = int(element[2])
                except (TypeError, ValueError):
                    pass
            if element[0] == "  +" or flag:
                output[element[1][:-1]] = temp
        else:
            if element[0] == "  +" or flag:
                output[element[1][:-1]] = generate_json_view(temp, True)
            elif element[0] == "   ":
                output[element[1][:-1]] = generate_json_view(temp)
                
    return output