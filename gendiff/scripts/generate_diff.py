def generate_difference(first_file, second_file):
    output = []

    for key in first_file.keys():
        if key in second_file:
            if first_file[key] == second_file[key]:
                output.append(("   ", key + ":", str(first_file[key]).lower()))
            else:
                output.append(("  -", key + ":", str(first_file[key]).lower()))
                output.append(("  +", key + ":", str(second_file[key]).lower()))
        else:
            output.append(("  -", key + ":", str(first_file[key]).lower()))

        for i in second_file.keys():
            if i not in first_file:
                output.append(("  +", i + ":", str(second_file[i]).lower()))

    sorted_output = sorted(set(output), key=lambda element: element[0],
                            reverse=True)
    sorted_output.sort(key=lambda element: element[1])
      
    return "{\n" + "\n".join([" ".join(i) for i in sorted_output]) + "\n}"
