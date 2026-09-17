"""
To-Do List Application
CodSoft Python Programming Internship - Task 1

A command-line To-Do List manager that lets a user create, view, update,
complete, and delete tasks. Tasks are stored in a local JSON file so the
list persists between runs.
"""

import json
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.json")


def load_tasks():
    """Load tasks from the JSON data file. Return an empty list if none exist."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def save_tasks(tasks):
    """Persist the current task list to the JSON data file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def add_task(tasks):
    title = input("Enter task title: ").strip()
    if not title:
        print("Task title cannot be empty.\n")
        return
    due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ").strip()
    task = {
        "id": (max((t["id"] for t in tasks), default=0) + 1),
        "title": title,
        "due_date": due_date or None,
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{title}' added.\n")


def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.\n")
        return
    print("\n--- YOUR TASKS ---")
    for t in tasks:
        status = "✔" if t["done"] else "✗"
        due = f" (due {t['due_date']})" if t.get("due_date") else ""
        print(f"[{t['id']}] {status} {t['title']}{due}")
    print()


def mark_done(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_id = int(input("Enter task ID to mark as done: "))
    except ValueError:
        print("Please enter a valid number.\n")
        return
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            save_tasks(tasks)
            print(f"Task '{t['title']}' marked as done.\n")
            return
    print("Task ID not found.\n")


def update_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_id = int(input("Enter task ID to update: "))
    except ValueError:
        print("Please enter a valid number.\n")
        return
    for t in tasks:
        if t["id"] == task_id:
            new_title = input(f"New title (leave blank to keep '{t['title']}'): ").strip()
            new_due = input("New due date YYYY-MM-DD (leave blank to keep current): ").strip()
            if new_title:
                t["title"] = new_title
            if new_due:
                t["due_date"] = new_due
            save_tasks(tasks)
            print("Task updated.\n")
            return
    print("Task ID not found.\n")


def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Please enter a valid number.\n")
        return
    for t in tasks:
        if t["id"] == task_id:
            tasks.remove(t)
            save_tasks(tasks)
            print(f"Task '{t['title']}' deleted.\n")
            return
    print("Task ID not found.\n")


def print_menu():
    print("===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")


def main():
    tasks = load_tasks()
    while True:
        print_menu()
        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            update_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.\n")


if __name__ == "__main__":
    main()
