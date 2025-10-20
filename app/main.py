import sys

from .command import Command


class TodoList:

    def __init__(self) -> None:
        self.command = Command()

    def print_menu(self) -> None:
        print("---menu----")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Completed")
        print("6. Exit")

    def run(self) -> None:

        while True:
            
            self.print_menu()
            choice = input("Select option: ")
            
            if choice == "1":
                self.command.add_task()
            elif choice == "2":
                self.command.show_tasks()
            elif choice == "3":
                self.command.update_task()
            elif choice == "4":
                self.command.delete_task()
            elif choice == "5":
                self.command.change_task_status()
            elif choice == "6":
                sys.exit()
            else:
                print("Bunaqa parametr mavjud emas!")                


            
            