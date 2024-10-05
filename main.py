import json
import os
from datetime import datetime
from typing import Any

file_path = "tasks.json"


def load_tasks() -> list[dict[str, Any]]:
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            tasks: list[dict[str, Any]] = json.load(file)
            return tasks
    else:
        with open(file_path, "w") as file:
            json.dump([], file, indent=4)
            return []


def save_tasks(tasks: list[dict[str, Any]]):
    with open(file_path, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(description: str):
    tasks: list[dict[str, Any]] = load_tasks()
    task_id: int = 0

    if tasks:
        task_id = tasks[-1]["id"] + 1

    new_task: dict[str, Any] = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": str(datetime.now()),
        "updatedAt": str(datetime.now()),
    }

    tasks.append(new_task)
    save_tasks(tasks)

    print(f"New task with ID {task_id} added.")


if __name__ == "__main__":
    user_command = input()

    space_index = user_command.find(" ")
    action = user_command[:space_index]

    if action == "add":
        task = user_command[space_index + 2 : -1]
        add_task(description=task)
