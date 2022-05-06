import os
import sqlite3
from datetime import datetime

from logic import settings
from logic.graphic import display_errors, display_messages


def is_exist_db():
    if not os.path.exists(settings.PATH_TODO_DB):
        os.makedirs(os.path.dirname(settings.PATH_TODO_DB), exist_ok=True)
        with open(settings.PATH_TODO_DB, "w") as f:
            f.write('')


def connect_user_db(nick):
    is_exist_db()
    con = sqlite3.connect(settings.PATH_TODO_DB)
    cursor = con.cursor()
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {nick} (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                                        timeCreated text,
                                                        taskName text, 
                                                        taskDescription text,
                                                        taskIsDone integer) ''')
    return con


def get_task_name():
    while True:
        inp = input("Task name:")
        if len(inp) < 3:
            display_errors.short_task_name()
        else:
            break
    return inp


def create_task(nick):
    conn = connect_user_db(nick)
    cursor = conn.cursor()

    task_name = get_task_name()
    task_description = input("Task description:")
    cursor.execute(f"INSERT INTO {nick}  "
                   f"(timeCreated,taskName,taskDescription, taskIsDone) "
                   f"values (?,?,?,?)",
                   (datetime.now(), task_name, task_description, 0))
    conn.commit()
    conn.close()
    display_messages.created_task()


def show_undone_task(CURRENT_USER):
    conn = connect_user_db(CURRENT_USER)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {CURRENT_USER} WHERE taskIsDone = 0", )
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(f"ID: {row[0]}\n"
                  f"Task name: {row[3]}\n"
                  f"Task description: {row[2]}\n"
                  f"Time created: {row[1]}")

    else:
        display_errors.no_tasks()


def show_all_task(CURRENT_USER):
    conn = connect_user_db(CURRENT_USER)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {CURRENT_USER}", )
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            is_task_done = False
            if row[4] == 1:
                is_task_done = True
            print(f"ID: {row[0]}\n"
                  f"Task name:{row[3]} \n"
                  f"Task description: {row[2]}\n"
                  f"Time created: {row[1]}\n"
                  f"Task is done: {is_task_done}")
    else:
        display_errors.no_tasks()


def get_id_task(max_id, min_id):
    inp = ''
    while not inp.isdigit():
        inp = input("ID:")
    if (int(inp) > max_id or int(inp) < min_id) and not isinstance(inp, int):
        while (int(inp) > max_id or int(inp) < min_id) and not isinstance(inp, int):
            inp = input("ID:")
    return int(inp)


def done_task(CURRENT_USER):
    conn = connect_user_db(CURRENT_USER)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {CURRENT_USER} WHERE taskIsDone = 0", )
    rows = cursor.fetchall()
    if rows:
        show_undone_task(CURRENT_USER)

        cursor.execute(f"SELECT id FROM {CURRENT_USER} "
                       f"WHERE (SELECT max(id) FROM {CURRENT_USER}) "
                       f"and taskIsDone = 0", )
        max_id = cursor.fetchall()

        cursor.execute(f"SELECT id FROM {CURRENT_USER} "
                       f"WHERE (SELECT min(id) FROM {CURRENT_USER}) "
                       f"and taskIsDone = 0", )
        min_id = cursor.fetchall()

        id = get_id_task(int(max_id[0][0]), int(min_id[0][0]))

        cursor.execute(f"SELECT * FROM {CURRENT_USER} WHERE id = {id}")
        task = cursor.fetchall()

        cursor.execute(f"UPDATE {CURRENT_USER} SET taskIsDone = 1 WHERE id = {id}")
        display_messages.task_done(task)
        conn.commit()
        conn.close()
    else:
        display_errors.no_tasks()


def task_edit_is_done():
    display_messages.edit_is_done()
    inp = ''
    while not inp.isdigit():
        inp = input("0 or 1:")
    if not inp == 1 or not inp == 0:
        inp = input("0 or 1:")
    return int(inp)


def edit_task(CURRENT_USER):
    conn = connect_user_db(CURRENT_USER)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {CURRENT_USER}", )
    rows = cursor.fetchall()
    if rows:
        show_all_task(CURRENT_USER)

        cursor.execute(f"SELECT id FROM {CURRENT_USER} "
                       f"WHERE (SELECT max(id) FROM {CURRENT_USER}) ")
        max_id = cursor.fetchall()

        cursor.execute(f"SELECT id FROM {CURRENT_USER} "
                       f"WHERE (SELECT min(id) FROM {CURRENT_USER}) ")
        min_id = cursor.fetchall()

        id = get_id_task(int(max_id[0][0]), int(min_id[0][0]))
        cursor.execute(f"SELECT * FROM {CURRENT_USER} WHERE id = {id}")
        task = cursor.fetchall()

        task_name = get_task_name()
        task_description = input("Task description:")
        is_done = task_edit_is_done()

        cursor.execute(f"UPDATE {CURRENT_USER} "
                       f"SET taskName = '{task_name}',"
                       f"taskDescription ='{task_description}',"
                       f"taskIsDone = {is_done} "
                       f"WHERE id = {id}")
        display_messages.edit(task)
        conn.commit()
        conn.close()
    else:
        display_errors.no_tasks()


def delete_task(CURRENT_USER):
    conn = connect_user_db(CURRENT_USER)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {CURRENT_USER}", )
    rows = cursor.fetchall()
    if rows:
        show_all_task(CURRENT_USER)

        cursor.execute(f"SELECT id FROM {CURRENT_USER} "
                       f"WHERE (SELECT max(id) FROM {CURRENT_USER}) ")
        max_id = cursor.fetchall()

        cursor.execute(f"SELECT id FROM {CURRENT_USER} "
                       f"WHERE (SELECT min(id) FROM {CURRENT_USER}) ")
        min_id = cursor.fetchall()
        id = get_id_task(int(max_id[0][0]), int(min_id[0][0]))

        cursor.execute(f"SELECT from {CURRENT_USER} where id = {id} ")
        task = cursor.fetchall()

        cursor.execute(f"DELETE from {CURRENT_USER} where id = {id} ")
        display_messages.deleted(task)
        conn.commit()
        conn.close()
    else:
        display_errors.no_tasks()
