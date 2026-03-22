import sys
import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            json.dump([], f)
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    tasks = load_tasks()
    
    new_task = {
        "id": len(tasks) + 1,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    
    tasks.append(new_task)
    save_tasks(tasks)
    
    print(f"Task added successfully (ID: {new_task['id']})")

def list_tasks(filter_status=None):
    tasks = load_tasks()
    
    for task in tasks:
        if filter_status and task["status"] != filter_status:
            continue
        print(task)

def update_task(task_id, new_desc):
    tasks = load_tasks()
    
    for task in tasks:
        if task["id"] == int(task_id):
            task["description"] = new_desc
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print("Task updated successfully")
            return
    print("Task not found")

def delete_task(task_id):
    tasks = load_tasks()
    
    tasks = [task for task in tasks if task["id"] != int(task_id)]
    save_tasks(tasks)
    print("Task deleted successfully")

def mark_in_progress(task_id):
    tasks = load_tasks()
    
    for task in tasks:
        if task["id"] == int(task_id):
            task["status"] = "in-progress"
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print("Task marked as in progress")
            return
    print("Task not found")

def mark_done(task_id):
    tasks = load_tasks()
    
    for task in tasks:
        if task["id"] == int(task_id):
            task["status"] = "done"
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print("Task marked as done")
            return   
    print("Task not found")

command = sys.argv[1] if len(sys.argv) > 1 else None

if command == "add":
    desc = sys.argv[2]
    add_task(desc)

elif command == "list":
    status = sys.argv[2] if len(sys.argv) > 2 else None
    list_tasks(status)

elif command == "update":
    update_task(sys.argv[2], sys.argv[3])

elif command == "delete":
    delete_task(sys.argv[2])

elif command == "mark-in-progress":
    mark_in_progress(sys.argv[2])

elif command == "mark-done":
    mark_done(sys.argv[2])

else:
    print("Command not recognized")