import json
import os
from datetime import datetime, date


class Storage:

    def __init__(self):
        self.DATABASE_URL = "database.json"

        if not os.path.exists(self.DATABASE_URL):
            with open(self.DATABASE_URL, "w") as f:
                json.dump([], f)
        else:
            try:
                with open(self.DATABASE_URL, 'r') as f:
                    json.load(f)
            except:
                with open(self.DATABASE_URL, "w") as f:
                    json.dump([], f)
    
    def read_database(self) -> list[dict]:
        with open(self.DATABASE_URL) as f:
            tasks = json.load(f)

        return tasks

    def save_database(self, tasks: list[dict]):
        with open(self.DATABASE_URL, "w") as f:
            json.dump(tasks, f, indent=4)

    def create_task(self, name: str, description: str, category: str, date: date) -> bool:
        tasks = self.read_database()

        last_task = max(tasks, key=lambda task: task['id'], default={"id": 0})
        tasks.append({
            "id": last_task["id"] + 1,
            "name": name,
            "description": description,
            "category": category,
            "due_date": date.strftime("%d/%m/%Y"),
            "created_date": datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
            "status": False,
        })

        self.save_database(tasks)

    def get_tasks(self, ):
        tasks = list(map(
            lambda task: {
                "id": task["id"],
                "name": task["name"],
                "description": task["description"],
                "category": task["category"],
                "due_date": datetime.strptime(task["due_date"], "%d/%m/%Y"),
                "created_date": datetime.strptime(task["created_date"], "%d/%m/%Y, %H:%M:%S"),
                "status": task["status"]
            },
            self.read_database(),
        ))

        return tasks