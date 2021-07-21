from rich.console import Console
from rich.table import Table
import os
from time import sleep
# on linux this is shit
# import keyboard
from pynput.keyboard import Listener


console    = Console()
TODO_items = []
DONE_items = []

cursor_position = {"first_column": True, "position": 0}

def add_todo_item(title: str) -> None:
    TODO_items.append(title)

def add_done_item(title: str) -> None:
    DONE_items.append(title)

def update() -> None:
    os.system("clear")
    table = Table(title="Todo App")
    table.add_column("TODO", justify="center", style="cyan", no_wrap=True)
    table.add_column("DONE", justify="center", style="cyan", no_wrap=True)
    bigger_number = len(TODO_items) if len(TODO_items) > len(DONE_items) else len(DONE_items)

    # this one has the problem and should be fixed cursor_position is not doing well here, when it goes out of index
    for i in range(0, bigger_number):
        if(cursor_position["first_column"] == True):
            if(cursor_position["position"] == i):
                try:
                    table.add_row(f"[bold blue] [ ] {TODO_items[i]}", f"[X] {DONE_items[i]}")
                except:
                    table.add_row(f"[bold blue] [ ] {TODO_items[i]}", "")
                continue
        else:
            if(cursor_position["position"] == i):
                try:
                    table.add_row(f"[ ] {TODO_items[i]}", f"[bold blue] [X] {DONE_items[i]}")
                except:
                    table.add_row("", f"[bold blue] [X] {DONE_items[i]}")
                continue
        try:
            table.add_row(f"[ ] {TODO_items[i]}", f"[X] {DONE_items[i]}")
        except:
            if(len(TODO_items) > len(DONE_items)):
                table.add_row(f"[ ] {TODO_items[i]}", "")
            else:
                table.add_row("", f"[X] {DONE_items[i]}")
    console.print(table)

def move_to_done(title: str) -> None:
    TODO_items.remove(title)
    DONE_items.append(title)
    update()

def move_to_todo(title: str) -> None:
    DONE_items.remove(title)
    TODO_items.append(title)
    update()


# def return_name_from_position(TODO_items, position) -> str:
#     result_items = []
#     count = 0
#     for i in TODO_items:
#         try:
#             result_items.append(TODO_items[co])
#         except:
#             break
#     return result_items[position]

add_todo_item("Kharid")
add_todo_item("Dars")
add_todo_item("Physic")
add_todo_item("Math")
add_todo_item("Class Zaban")
add_done_item("Ketab Khandan")
add_done_item("Playing chess as usual")

update()

def on_press(key):
    if key.char == "u":
        # TODO change 0 if needed
        if(cursor_position["position"] != 0):
            cursor_position["position"] -= 1
        update()
    if key.char == "e":
        if(cursor_position["first_column"]):
            if(cursor_position["position"] != len(TODO_items) - 1):
                cursor_position["position"] += 1
        else:
            if(cursor_position["position"] != len(DONE_items) - 1):
                cursor_position["position"] += 1
        update()
    if key.char == "i":
        cursor_position["first_column"] = False
        if(cursor_position["position"] > len(DONE_items) - 1):
            cursor_position["position"] = len(DONE_items) - 1
        update()
    if key.char == "n":
        cursor_position["first_column"] = True
        if(cursor_position["position"] > len(TODO_items) - 1):
            cursor_position["position"] = len(TODO_items) - 1
        update()
    if key.char == "t":
        if(cursor_position["first_column"] == True):
            # Not needed anymore
            # title = return_name_from_position(TODO_items, cursor_position["position"])
            # move_to_done(title)
            move_to_done(TODO_items[cursor_position["position"]])
        else:
            move_to_todo(DONE_items[cursor_position["position"]])

with Listener(on_press=on_press) as listener:
    listener.join()
