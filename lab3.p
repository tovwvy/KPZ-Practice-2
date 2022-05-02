from palindrom import palindrom
from printOS import get_os
from validatorIP import validate_ip

print(palindrom("rreeer "))

print(validate_ip("2.2.2.02"))
print(validate_ip("2.2.2.366:1111"))
print(validate_ip("2.2.2.136"))

print(get_os())





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
                if value == value[::-1]:
                    result.append(value)
    return 
    
    
    import platform


def get_os():
    os = platform.system()
    if os == "Windows":
        return "Mac"
    elif os == "linux":
        pass
    else:
        return 
        
        
        
        
        import socket


def validate_ip(ip_address):
    if len(ip_address) < 7:
        raise Exception("The argument must contain a string of more than 7 characters")
    if not isinstance(ip_address, str):
        raise Exception("The argument must contain the string ")

    try:
        socket.inet_aton(ip_address)
        return True
    except:
        return False
