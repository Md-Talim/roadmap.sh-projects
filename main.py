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


def update_task(id: int, new_description: str):
    tasks: list[dict[str, Any]] = load_tasks()

    if not tasks:
        print("There are currently no tasks to update.")
        return

    for task in tasks:
        if task["id"] == id:
            task["description"] = new_description
            task["updatedAt"] = str(datetime.now())
            save_tasks(tasks)
            print(f"Task with ID {id} got updated.")
            return

    print(f"No task found with ID: {id}")


def delete_task(id: int):
    tasks: list[dict[str, Any]] = load_tasks()

    if not tasks:
        print("There are currently no tasks to delete.")
        return

    for i, task in enumerate(tasks):
        if task["id"] == id:
            del tasks[i]
            save_tasks(tasks)
            print(f"Task with ID {id} has been successfully deleted.")
            return

    print(f"Task with ID {id} not found.")


if __name__ == "__main__":
    user_command = input()

    space_index = user_command.find(" ")
    action = user_command[:space_index]

    if action == "add":
        task = user_command[space_index + 2 : -1]
        add_task(description=task)
    elif action == "update":
        splitted_command = user_command.split(' "')

        new_description = splitted_command[1]
        new_description = new_description[:-1]

        task_id = int(splitted_command[0].split(" ")[1])
        update_task(task_id, new_description)
    elif action == "delete":
        task_id = int(user_command[space_index + 1 :])
        delete_task(task_id)
