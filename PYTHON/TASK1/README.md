# Task 1 — To-Do List Application

A command-line To-Do List manager built in Python for the **CodSoft Python
Programming Internship**. It lets you create, view, update, mark complete,
and delete tasks. All tasks are saved to `tasks.json` so your list persists
between runs.

## Features
- Add a task with an optional due date
- View all tasks with their status (done / not done)
- Mark a task as done
- Update a task's title or due date
- Delete a task
- Data automatically saved to and loaded from `tasks.json`

## How to Run
```bash
python todo.py
```
No external libraries are required — the project only uses Python's
standard library (`json`, `os`, `datetime`).

## Example Session
```
===== TO-DO LIST MENU =====
1. Add Task
2. View Tasks
3. Mark Task as Done
4. Update Task
5. Delete Task
6. Exit
Choose an option (1-6): 2

--- YOUR TASKS ---
[1] ✗ Complete Python Programming Task 1 (due 2026-09-20)
[2] ✗ Push code to GitHub repo CODSOFT_TASKSNO (due 2026-09-22)
[3] ✔ Record demo video for LinkedIn
```

## Files
| File | Description |
|------|-------------|
| `todo.py` | Main application source code |
| `tasks.json` | Sample/persisted task data |
| `README.md` | This file |

## Project Structure Notes
- `add_task`, `view_tasks`, `mark_done`, `update_task`, `delete_task` are
  each isolated functions to keep the code modular and testable.
- Data is stored as JSON, keeping the project dependency-free while still
  demonstrating file I/O and persistence.

---
Part of the **#codsoft** Python Programming virtual internship.
