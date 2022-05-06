import re

from logic import task
from logic.graphic import display_messages


def main_menu(CURRENT_USER):
    pattern_help = re.compile(r"help")
    pattern_create = re.compile(r"create")
    pattern_show_task = re.compile(r"show")
    pattern_show_all_task = re.compile(r"showall")
    pattern_edit = re.compile(r"edit")
    pattern_done = re.compile(r"done")
    pattern_exit = re.compile(r"exit")
    pattern_delete = re.compile(r"delete")
    inp = input("Command: ")
    if pattern_exit.match(inp):
        exit()
    elif pattern_help.match(inp):
        display_messages.help_menu()
    elif pattern_create.match(inp):
        task.create_task(CURRENT_USER)
    elif pattern_show_all_task.match(inp):
        task.show_all_task(CURRENT_USER)
    elif pattern_show_task.match(inp):
        task.show_undone_task(CURRENT_USER)
    elif pattern_edit.match(inp):
        task.edit_task(CURRENT_USER)
    elif pattern_done.match(inp):
        task.done_task(CURRENT_USER)
    elif pattern_delete.match(inp):
        task.delete_task(CURRENT_USER)
    else:
        display_messages.incorrect_command()
