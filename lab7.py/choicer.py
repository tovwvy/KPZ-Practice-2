from logic import auth
from logic.graphic import display_errors


def log_or_create():
    inp = input("Choose: ")
    if inp.strip(" ") == "1":
        auth.logging()
    elif inp.strip(" ") == "2":
        auth.create_account()
    elif inp.strip(" ") == "0":
        exit()
    else:
        display_errors.error_log_or_create(inp)
        log_or_create()
