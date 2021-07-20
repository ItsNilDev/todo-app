from rich.console import Console
from rich.table import Table

table = Table(title="Todo App")

table.add_column("TODO", justify="center", style="cyan", no_wrap=True)
table.add_column("DONE", justify="center", style="cyan", no_wrap=True)

TODO_items = []
DONE_items = []

def add_todo_item(title: str) -> None:
    TODO_items.append(title)

def add_done_item(title: str) -> None:
    DONE_items.append(title)
    # table.add_row("", f"[X] {title}")

def update() -> None:
    bigger_number = len(TODO_items) if len(TODO_items) > len(DONE_items) else len(DONE_items)
    for i in range(0, bigger_number):
        print(i)
        try: 
            table.add_row(f"[ ] {TODO_items[i]}", f"[X] {DONE_items[i]}")
        except:
            if(len(TODO_items) > len(DONE_items)):
                table.add_row(f"[ ] {TODO_items[i]}", "")       
            else:
                table.add_row("", f"[X] {DONE_items[i]}")       

        



add_done_item("buy milk")
add_done_item("Use a version control")
add_done_item("Use a version control")
add_todo_item("Lorem ipsum dolor sit ametconsectetur")
add_done_item("Use a version control")
add_todo_item("adipiscing elit consectetur adipiscing")
add_todo_item("prove that 2+2 is not 5")
update()

console = Console()
console.print(table)