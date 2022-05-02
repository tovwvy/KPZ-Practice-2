import re


def palindrom(input):
    if not isinstance(input, str):
        raise Exception("The argument must contain the string ")
    if len(input) < 2:
        raise Exception("The argument must contain a string of more than 2 characters")
    result = []
    array = re.findall(r"[\w']+", input)
    for value in array:
        if len(value) > 1:
            if len(value) > 1:
                if value.lower() == value[::-1].lower():
                    result.append(value)
    return 
