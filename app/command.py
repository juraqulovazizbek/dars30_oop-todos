from datetime import datetime

from rich.console import Console
from rich.table import Table

from .storage import Storage


class Command:
    def __init__(self):
        self.tasks = []
        self.storage = Storage()

    def add_task(self):
        name = input("Task name: ").strip().capitalize()
        description = input("Description: ").strip().capitalize()
        category = input("Category: ").strip().title()
        due_date = input("Date (example: 2025-10-11): ")

        due_date = datetime.strptime(due_date, "%Y-%m-%d")
        if due_date < datetime.now():
            print("Date shoulde be greater than or equal to now.")
            return

        self.storage.create_task(name, description, category, due_date)
        print("✅ Vazifa muvaffaqiyatli qo'shildi!")

    def show_tasks(self):
        tasks = self.storage.get_tasks()

        console = Console()

        table = Table(title="All Tasks")
        table.add_column("Number")
        table.add_column("Name")
        table.add_column("Category")
        table.add_column("Due Date")

        for num, task in enumerate(tasks, start=1):
            du_date = task["due_date"].strftime("%d/%m/%Y")
            table.add_row(str(num), task["name"], task["category"], du_date)
        
        console.print(table)

        num = int(input("Task detail: "))
        task = tasks[num - 1]
        
        status = "❌Incompleted"
        if task["status"]:
            status = "✅ Completed"
        du_date = task["due_date"].strftime("%d/%m/%Y")
        created_date = task["created_date"].strftime("%d/%m/%Y, %H:%M:%S")

        print(f"Task name: {task['name']}")
        print(f"Description: {task['description']}")
        print(f"Category: {task['category']}")
        print(f"Status: {status}")
        print(f"Due Date: {du_date}")
        print(f"Created Date: {created_date}")
        
        print()

            