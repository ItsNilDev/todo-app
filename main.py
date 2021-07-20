from rich.console import Console
from rich.table import Table
import os
import keyboard

console    = Console()
TODO_items = []
DONE_items = []

cursor_position = {"first_row": True, "position": 0}

def add_todo_item(title: str) -> None:
    TODO_items.append(title)

def add_done_item(title: str) -> None:
    DONE_items.append(title)

def move_to_done(title: str) -> None:
    TODO_items.remove(title)
    DONE_items.append(title)
    update()

def update() -> None:
    os.system("clear")
    table = Table(title="Todo App")
    table.add_column("TODO", justify="center", style="cyan", no_wrap=True)
    table.add_column("DONE", justify="center", style="cyan", no_wrap=True)
    bigger_number = len(TODO_items) if len(TODO_items) > len(DONE_items) else len(DONE_items) 

    for i in range(0, bigger_number):
        if(cursor_position["first_row"] == True):
            if(cursor_position["position"] == i):
                try:
                    table.add_row(f"* [ ] {TODO_items[i]}", f"[X] {DONE_items[i]}")
                except:
                    table.add_row(f"* [ ] {TODO_items[i]}", "")
                continue
        else:
            if(cursor_position["position"] == i):
                try:
                    table.add_row(f"[ ] {TODO_items[i]}", f"* [X] {DONE_items[i]}")
                except:
                    table.add_row("", f"* [X] {DONE_items[i]}")
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



add_todo_item("buy milk")
add_done_item("Use a version control")
add_done_item("Use a version control")
add_todo_item("Lorem ipsum dolor sit")
add_done_item("Use a version control")
add_todo_item("adipiscing elit consectetur adipiscing")
add_todo_item("prove that 2+2 is not 5")
update()

move_to_done("buy milk")
move_to_done("adipiscing elit consectetur adipiscing")

while True:
    if keyboard.read_key() == "e":
        cursor_position["position"] += 1
        update()
    if keyboard.read_key() == "u":
        cursor_position["position"] -= 1
        update()
    if keyboard.read_key() == "i":
        print("Hello")
        cursor_position["first_row"] = False
        update()
    if keyboard.read_key() == "n":
        cursor_position["first_row"] = True
        update()

    