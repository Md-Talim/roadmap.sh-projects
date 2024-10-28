# Task Tracker CLI

A simple Command Line Interface (CLI) tool to help you track and manage your tasks. This project allows you to add, update, delete, and mark tasks as "in-progress" or "done." It also lets you list tasks based on their status, helping you stay organized and productive.

This project was inspired by the **Task Tracker** project from [roadmap.sh](https://roadmap.sh/projects/task-tracker).

## Features

- **Add Tasks**: Create new tasks with unique IDs.
- **Update Tasks**: Modify the description of an existing task.
- **Delete Tasks**: Remove tasks by their ID.
- **Mark Tasks as In-Progress or Done**: Change the status of tasks as you work on them.
- **List Tasks**: View all tasks or filter them by their status (`todo`, `in-progress`, `done`).

## Task Properties

Each task has the following properties:

- **id**: A unique identifier for the task.
- **description**: A short description of the task.
- **status**: The current status of the task. It can be one of the following:
  - `todo` (📝)
  - `in-progress` (⏳)
  - `done` (✅)
- **createdAt**: The date and time when the task was created.
- **updatedAt**: The date and time when the task was last updated.

All tasks are stored in a `tasks.json` file, which is created automatically if it does not exist.

## Usage

This CLI tool accepts user commands from the terminal to manage tasks. Below are the available commands and their usage.

### ➕ Add a New Task

To add a new task, use the `add` command followed by the task description in quotes.

```bash
task-cli add "buy groceries"
```

### ⌛ Update a Task

To update the description of an existing task, use the `update` command followed by the task ID and the new description in quotes.

```bash
task-cli update 1 "buy groceries and cook dinner"
```

### 🗑️ Delete a Task

To delete a task, use the `delete` command followed by the task ID.

```bash
task-cli delete 1
```

### ⏳ Mark a Task as In-Progress

To mark a task as "in-progress," use the `mark-in-progress` command followed by the task ID.

```bash
task-cli mark-in-progress 1
```

### ✅ Mark a Task as Done

To mark a task as "done," use the `mark-done` command followed by the task ID.

```bash
task-cli mark-done 1
```

### 📋 List All Tasks

To list all tasks, use the `list` command. Tasks will be displayed with their descriptions, IDs, and statuses, with emojis for quick reference.

```bash
task-cli list
```

### 📊 List Tasks by Status

To list tasks filtered by their status, use the `list` command followed by the status (`todo`, `in-progress`, or `done`).

- List all tasks that are **todo**:
  ```bash
  task-cli list todo
  ```
- List all tasks that are **in-progress**:
  ```bash
  task-cli list in-progress
  ```
- List all tasks that are **done**:
  ```bash
  task-cli list done
  ```

## Example Commands

```bash
# Adding a new task
task-cli add "Clean the house"

# Updating an existing task
task-cli update 2 "Clean the house and organize the garage"

# Deleting a task
task-cli delete 2

# Marking a task as in-progress
task-cli mark-in-progress 3

# Marking a task as done
task-cli mark-done 3

# Listing all tasks
task-cli list

# Listing tasks by specific status
task-cli list done
```

### Error Handling

- If you try to update, delete, or mark a task that doesn’t exist, you’ll receive a message saying the task with the given ID was not found.
- If no tasks exist, the system will notify you that there are currently no tasks available.

### File Storage

All tasks are stored in a JSON file (`tasks.json`) in the current directory. If the file doesn’t exist, it will be automatically created when the application is first run.
