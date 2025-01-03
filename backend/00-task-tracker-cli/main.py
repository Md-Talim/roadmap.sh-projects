import json
import os
from datetime import datetime
from typing import Any
import argparse

FILE_PATH = "tasks.json"
TASK_STATUS = ["todo", "in-progress", "done"]


def load_tasks() -> list[dict[str, Any]]:
    """
    Loads tasks from the JSON file.

    If the file exists, it reads and returns the list of tasks. If the file
    does not exist, it creates an empty file and returns an empty list.
    """
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r", encoding="UTF-8") as file:
            tasks: list[dict[str, Any]] = json.load(file)
            return tasks
    else:
        with open(FILE_PATH, "w", encoding="UTF-8") as file:
            json.dump([], file, indent=4)
            return []


def save_tasks(tasks: list[dict[str, Any]]):
    """
    Saves the current list of tasks to the JSON file.
    """
    with open(FILE_PATH, "w", encoding="UTF-8") as file:
        json.dump(tasks, file, indent=4)


def generate_task_id(tasks: list[dict[str, Any]]) -> int:
    """
    Generate a unique ID for a new task.

    The ID is generated by adding 1 to the last task's ID. If no tasks exist, it returns 0.
    """
    if tasks:
        return tasks[-1]["id"] + 1
    return 0


def find_task_by_id(tasks: list[dict[str, Any]], task_id: int) -> dict[str, Any] | None:
    """
    Finds task by id using binary search.
    """
    high = len(tasks) - 1
    low = 0

    while low <= high:
        mid = (low + high) // 2
        current_task = tasks[mid]

        if current_task["id"] == task_id:
            return current_task

        if current_task["id"] < task_id:
            low = mid + 1
        else:
            high = mid - 1

    return None  # Task with the given ID was not found


def add_task(description: str):
    """
    Add a new task to the task list.
    """
    tasks: list[dict[str, Any]] = load_tasks()
    task_id: int = generate_task_id(tasks)

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


def update_task(task_id: int, new_description: str):
    """
    Updates the description of a task by its ID.

    If the task exists, its description is updated, and the `updatedAt` timestamp is refreshed.
    """
    tasks: list[dict[str, Any]] = load_tasks()

    if not tasks:
        print("There are currently no tasks to update.")
        return

    task = find_task_by_id(tasks, task_id)

    if task:
        task["description"] = new_description
        task["updatedAt"] = str(datetime.now())
        save_tasks(tasks)
        print(f"Task with ID {task_id} updated.")
    else:
        print(f"No task found with ID: {id}")


def delete_task(task_id: int):
    """
    Deletes a task by its `ID`.

    If the task with the given ID exists, it is removed from the task list.
    """
    tasks: list[dict[str, Any]] = load_tasks()

    if not tasks:
        print("There are currently no tasks to delete.")
        return

    task = find_task_by_id(tasks, task_id)

    if task:
        tasks.remove(task)
        save_tasks(tasks)
        print(f"Task with ID {task_id} has been deleted.")
    else:
        print(f"Task with ID {task_id} not found.")


def update_task_status(task_id: int, new_status: str):
    """
    Updates the status of a task by its `ID`.

    The task status can be updated to:
    - `todo`
    - `in-progress`
    - `done`.

    If the task exists, its status is updated, and the `updatedAt` timestamp is refreshed.
    """
    tasks: list[dict[str, Any]] = load_tasks()

    if not tasks:
        print("There are currently no tasks to update.")
        return

    task = find_task_by_id(tasks, task_id)

    if not new_status in TASK_STATUS:
        print("Enter one of the following status: 'todo', 'in-progress', or 'done'.")
        return

    if task:
        old_status = task["status"]
        task["status"] = new_status
        task["updatedAt"] = str(datetime.now())
        save_tasks(tasks)
        print(f"Task {task_id} status updated from '{old_status}' to '{new_status}'.")
    else:
        print(f"No task found with ID: {task_id}.")


def list_tasks(status: str):
    """
    List tasks with a specific status or all tasks.
    Filters tasks based on the status (`todo`, `in-progress`, or `done`)
    Lists all tasks if no status is provided.
    """
    tasks: list[dict[str, Any]] = load_tasks()

    if not tasks:
        print("There are currently no tasks to print.")
        return

    if status and status not in TASK_STATUS:
        print(f"Invalid status '{status}'. Please use one of: {', '.join(TASK_STATUS)}")
        return

    status_emojis = {"todo": "📝", "in-progress": "⏳", "done": "✅"}
    tasks_to_print = [task for task in tasks if task["status"] == status or not status]

    if tasks_to_print:
        for task in tasks_to_print:
            emoji = status_emojis.get(task["status"], "")
            print(f"{emoji} {task['description']} (ID: {task['id']})")
    else:
        print(
            f"No tasks found with status '{status}'."
            if status
            else "No tasks available."
        )


def main():
    """
    The main entry point for the task CLI application.
    """
    parser = argparse.ArgumentParser(description="Task management CLI")

    # Create subparsers for individual commands
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add subcommand
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="Description of the task")

    # Update subcommand
    update_parser = subparsers.add_parser("update", help="Update an existing task")
    update_parser.add_argument("task_id", type=int, help="ID of the task to update")
    update_parser.add_argument("description", type=str, help="New task description")

    # Delete subcommand
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("task_id", type=int, help="ID of the task to delete")

    # Mark in-progress subcommand
    mark_in_progress_parser = subparsers.add_parser(
        "mark-in-progress", help="Mark task as in-progress"
    )
    mark_in_progress_parser.add_argument("task_id", type=int, help="ID of the task")

    # Mark done subcommand
    mark_done_parser = subparsers.add_parser("mark-done", help="Mark task as done")
    mark_done_parser.add_argument("task_id", type=int, help="ID of the task")

    # List subcommand
    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument(
        "status", type=str, nargs="?", default="", help="Filter tasks by status"
    )

    args = parser.parse_args()

    # Handle commands
    if args.command == "add":
        add_task(args.description)
    elif args.command == "update":
        update_task(args.task_id, args.description)
    elif args.command == "delete":
        delete_task(args.task_id)
    elif args.command == "mark-in-progress":
        update_task_status(args.task_id, "in-progress")
    elif args.command == "mark-done":
        update_task_status(args.task_id, "done")
    elif args.command == "list":
        list_tasks(args.status)


if __name__ == "__main__":
    main()
