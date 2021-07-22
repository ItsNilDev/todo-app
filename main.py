from rich.console import Console
from rich.table import Table
import os
from time import sleep
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

def move_to_todo(title: str) -> None:
    DONE_items.remove(title)
    TODO_items.append(title)

def remove_from_todo(title: str) -> None:
    TODO_items.remove(title)

def remove_from_done(title: str) -> None:
    DONE_items.remove(title)

add_todo_item("Prove that 2+2")
add_done_item("Meth")
add_done_item("buy milk")

update()

# I use colemak.
def on_press(key):
    if key.char == "i":
        # TODO change 0 if needed
        if(cursor_position["position"] != 0):
            cursor_position["position"] -= 1
        update()
    if key.char == "k":
        if(cursor_position["first_column"]):
            if(cursor_position["position"] != len(TODO_items) - 1):
                cursor_position["position"] += 1
        else:
            if(cursor_position["position"] != len(DONE_items) - 1):
                cursor_position["position"] += 1
        update()
    if key.char == "l":
        cursor_position["first_column"] = False
        if(cursor_position["position"] > len(DONE_items) - 1):
            cursor_position["position"] = len(DONE_items) - 1
        update()
    if key.char == "j":
        cursor_position["first_column"] = True
        if(cursor_position["position"] > len(TODO_items) - 1):
            cursor_position["position"] = len(TODO_items) - 1
        update()
    if key.char == "f":
        if(cursor_position["first_column"] == True):
            move_to_done(TODO_items[cursor_position["position"]])
            if(cursor_position["position"] > len(TODO_items) - 1):
                if(TODO_items != []):
                    cursor_position["position"] = len(TODO_items) - 1
                else:
                    cursor_position["first_column"] = False
                    cursor_position["position"] = 0
            update()
        else:
            move_to_todo(DONE_items[cursor_position["position"]])
            if(cursor_position["position"] > len(DONE_items) - 1):
                if(DONE_items != []):
                    cursor_position["position"] = len(DONE_items) - 1
                else:
                    cursor_position["first_column"] = True
                    cursor_position["position"] = 0
            update()
    if key.char == "s":
        # if(cursor_position["first_column"]):
        #     remove_from_todo(TODO_items[cursor_position["position"]])
        #     if(cursor_position["position"] > len(TODO_items) - 1):
        #         if(TODO_items != []):
        #             cursor_position["position"] = len(TODO_items) - 1
        #         else:
        #             cursor_position["first_column"] = False
        #             cursor_position["position"] = 0
        #     update()
        # if(cursor_position["first_column"] == False):
        #     remove_from_todo(DONE_items[cursor_position["position"]])
        #     if(cursor_position["position"] > len(DONE_items) - 1):
        #         if(DONE_items != []):
        #             cursor_position["position"] = len(DONE_items) - 1
        #         else:
        #             cursor_position["first_column"] = True
        #             cursor_position["position"] = 0
        #     update()
        pass

with Listener(on_press=on_press) as listener:
    listener.join()
