from rich.console import Console
from rich.rule import Rule
import os
from time import sleep

# initial setup
os.system("clear")
console = Console(width=30)

def setup() -> None:
    os.system("clear")
    console.print("[bold blue]|", end='')
    console.print(Rule("TODO", end=''))

    console.print("[bold blue]|  |", end='')

    console.print(Rule("Done", end=''))
    console.print("[bold blue]|", end='\n  ')

TODO_items = []
DONE_items = []

def update() -> None:
    # Something is tickling me and telling me that it's not the correct way of doing it...
    if(DONE_items == []):
        for i in TODO_items:
            console.print(f"[ ] {i}", end='\n  ')
    else:
        bigger_number = len(TODO_items) if len(TODO_items) > len(DONE_items) \
                        else len(DONE_items)
        for i in range(0, bigger_number):
            try:
                console.print(f"[ ] {TODO_items[i]}", end='                         ')
            except:
                console.print("        ", end='       ')
                console.print("        ", end='       ')
            console.print(f"[X] {DONE_items[i]}", end='\n  ')

# Add item to each list
def add_todo_item(title: str) -> None:
    TODO_items.append(title)
    setup()
    update()

def add_done_item(title: str) -> None:
    DONE_items.append(title)
    setup()
    update()

def delete_todo_item(title: str) -> None:
    TODO_items.remove(title)
    setup()
    update()

# def move_to_done(title: str) -> None:
#     delete_todo_item(title)


setup()
add_todo_item("Prove that 2+2 is not 5")
add_done_item("Add a version control")
add_done_item("Make this project public")
add_todo_item("Buy milk")