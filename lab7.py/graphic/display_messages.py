def greeting():
    print("Greetings. This is a super duper todo list. Please login or create an account.\n")


def log_or_create():
    print("1. To login.\n"
          "2. To create.\n"
          "0. Terminate program")


def greeting_main_menu():
    print("You can type help for commands")


def help_menu():
    print("help - this menu\n"
          "create - create new task\n"
          "show - show undone tasks\n"
          "showall - show all tasks\n"
          "edit - edit task by id\n"
          "done - make task is done by id\n"
          "delete - delete task by id")


def created_task():
    print("Task created")


def task_done(task):
    print(f"Your task with ID {task[0][0]} is done")


def edit(task):
    print(f"Your task with ID {task[0][0]} is edit")


def logged():
    print("You logged!")


def incorrect_command():
    print("Incorrect command. You can type help for commands")


def deleted(task):
    print(f"Your task with ID {task[0][0]} is deleted")


def edit_is_done():
    print("Type 0 or 1.")
