def error_log_or_create(inp):
    print(f"Error input. Possible choices it's 1, 2 or 0. You're input: {inp}")


def short_username(inp):
    print(f"Error input. Short length. Need more than three letters or numbers.  You're length: {len(inp)}")


def spacebar_username(inp):
    print(f"Error input. There is a spacebar when entering.  You're input: [{inp}]")


def non_word_character(inp):
    print(f"Error input. Non-word character detected.  You're input: {inp}")


def short_password(inp):
    print(f"Error input. Short length. Need more than six symbols.  You're length: {len(inp)}")


def not_find_username():
    print("There is no user with that username and password")


def not_unique_username():
    print("Error input. The following nickname exists in the database")


def short_task_name():
    print("Error input. Short task name. Need more than three symbols.")


def no_tasks():
    print("No tasks. Create a task before edit/done/show/delete")
