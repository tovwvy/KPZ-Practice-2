def validate_ip(ip_address):
   ip_validate = False
   try:
      ip = ipaddress.ip_address(ip_address)
      ip_validate = True
   except ValueError:
      ip_validate = False

   return ip_validate




@pytest.mark.parametrize("validate_ip_func_arg, result", [("192.156", False), ("-1.168.1.42", False),
                                                          ("192.399.1.40", False),
                                                          ("192.176.-44.42", False),
                                                          ("192.147.1.420", False)])
def test_validate_ip(validate_ip_func_arg, result):
    assert validate_ip_func_arg != ''
    assert validate_ip(validate_ip_func_arg) == result


def get_os():
   return platform.system()


def test_get_os():
   assert get_os() == "Windows"
