import os.path
import re
import sqlite3

from cryptography.fernet import Fernet
from logic import settings
from logic.graphic import display_errors, display_messages


def connect_user_db():
    is_exist_db()
    con = sqlite3.connect(settings.PATH_USER_DB)
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (nickname text, password text) ''')
    return con


def is_unique(inp):
    con = connect_user_db()
    cursor = con.cursor()
    f = Fernet(settings.SECRET_KEY)

    cursor.execute("SELECT nickname FROM users")
    rows_nickname = cursor.fetchall()
    for row in rows_nickname:
        if inp == f.decrypt(row[0].encode()).decode():
            return False
    return True


def get_nick(is_logging):
    while True:
        inp = input("Username: ")
        if inp == "0":
            exit()
        elif re.match(r"\s", inp):
            display_errors.spacebar_username(inp)
        elif len(inp) < 3:
            display_errors.short_username(inp)
        elif not is_unique(inp) and not is_logging:
            display_errors.not_unique_username()
        elif not inp.isalnum():
            display_errors.non_word_character(inp)
        else:
            break

    return inp


def get_pass():
    while True:
        inp = input("Password: ")
        if len(inp) < 6:
            display_errors.short_password(inp)
        elif inp == "0":
            exit()
        else:
            break
    return inp


def is_exist_db():
    if not os.path.exists(settings.PATH_USER_DB):
        os.makedirs(os.path.dirname(settings.PATH_USER_DB), exist_ok=True)
        with open(settings.PATH_USER_DB, "w") as f:
            f.write('')


def create_account():
    conn = connect_user_db()
    cursor = conn.cursor()
    nick = get_nick(False)
    password = get_pass()
    f = Fernet(settings.SECRET_KEY)
    cursor.execute("INSERT INTO users VALUES(?,?);", (f.encrypt(nick.encode()).decode(),
                                                      f.encrypt(password.encode()).decode()))
    conn.commit()
    conn.close()
    settings.CURRENT_USER = nick


def logging():
    conn = connect_user_db()
    cursor = conn.cursor()
    f = Fernet(settings.SECRET_KEY)

    cursor.execute("SELECT nickname FROM users")
    rows_nickname = cursor.fetchall()
    while True:
        is_find_nick = False
        is_find_password = False
        nickname = get_nick(True)
        if not is_find_nick:
            for row in rows_nickname:
                if nickname == f.decrypt(row[0].encode()).decode():
                    is_find_nick = True
                    settings.CURRENT_USER = nickname

        if is_find_nick:
            cursor.execute("SELECT password FROM users")
            rows_password = cursor.fetchall()
            password = get_pass()
            for row in rows_password:
                if password == f.decrypt(row[0].encode()).decode():
                    is_find_password = True

        if is_find_password:
            display_messages.logged()
            break
        else:
            display_errors.not_find_username()
