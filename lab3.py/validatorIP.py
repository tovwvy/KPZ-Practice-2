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
