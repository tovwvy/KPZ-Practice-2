def validate_ip(ip_address):
    ip_validate = False
    try:
        ip = ipaddress.ip_address(ip_address)
        ip_validate = True
    except ValueError:
        ip_validate = False

    return ip_validate


validate_ip("192.172.2.43")
validate_ip("192.172.2.335")


def get_os():
    return platform.system()
get_os()
