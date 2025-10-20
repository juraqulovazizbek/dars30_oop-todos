from datetime import datetime

from rich.console import Console
from rich.table import Table
console=Console()
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
        print("Vazifa muvaffaqiyatli qo'shildi!")

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
        
        status = "Incompleted"
        if task["status"]:
            status = " Completed"
        du_date = task["due_date"].strftime("%d/%m/%Y")
        created_date = task["created_date"].strftime("%d/%m/%Y, %H:%M:%S")

        print(f"Task name: {task['name']}")
        print(f"Description: {task['description']}")
        print(f"Category: {task['category']}")
        print(f"Status: {status}")
        print(f"Due Date: {du_date}")
        print(f"Created Date: {created_date}")

    def update_task(self):
        tasks = self.storage.read_database()
        if not tasks:
            console.print("[red]Tasklar mavjud emas![/red]")
            return

        try:
            task_id = int(input("Yangilamoqchi bo‘lgan task ID sini kiriting: "))
        except ValueError:
            console.print("[red] ID raqam bo‘lishi kerak![/red]")
            return

        for task in tasks:
            if task["id"] == task_id:
                console.print(f"[cyan]Hozirgi ma'lumotlar:[/cyan]")
                console.print(f"Name: {task['name']}")
                console.print(f"Description: {task['description']}")
                console.print(f"Category: {task['category']}")

                new_name = input("Yangi name: ").strip()
                new_description = input("Yangi description: ").strip()
                new_category = input("Yangi category: ").strip()

                if new_name:
                    task["name"] = new_name.capitalize()
                if new_description:
                    task["description"] = new_description.capitalize()
                if new_category:
                    task["category"] = new_category.title()

                self.storage.save_database(tasks)
                console.print("[green] Task muvaffaqiyatli yangilandi![/green]")
                return

        console.print("[red] Bunday ID topilmadi![/red]")

    def delete_task(self):
        tasks = self.storage.read_database()
        if not tasks:
            console.print("[red]Tasklar mavjud emas![/red]")
            return

        name = input("O‘chirmoqchi bo‘lgan task nomini kiriting: ").strip()

        for task in tasks:
            if task["name"].lower() == name.lower():
                tasks.remove(task)
                self.storage.save_database(tasks)
                console.print(f"[blue]{task['name']} task o‘chirildi![/blue]")
                return

        console.print("[red] Bunday nomli task topilmadi![/red]")

    def change_task_status(self):
        tasks = self.storage.read_database()
        if not tasks:
            console.print("[red]Tasklar mavjud emas![/red]")
            return

        task_name = input("Task nomini yozing: ").strip().capitalize()

        for task in tasks:
            if task["name"] == task_name:
                task["status"] = not task["status"]  
                self.storage.save_database(tasks)
                holat = "Bajarilgan" if task["status"] else " Bajarilmagan"
                console.print(f"[blue]'{task_name}' task holati yangilandi![/blue] ({holat})")
                return

        console.print("[red] Bunday nomli task topilmadi.[/red]")        