import json
import os

# Defining database file name
DATA_FILE = 'tasks.json'

def load_tasks() -> list:
    """Load tasks from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (son.JSONDecodeError, FileNotFoundError):
        return []
    
def save_tasks(tasks: list) -> None:
    """Save tasks to the JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)
        
def add_task(description: str) -> None:
    """Add a new task to the list."""
    tasks = load_tasks()
    new_task = {
        'description': description,
        'completed': False
    }
    tasks.append(new_task)
    save_tasks(tasks)