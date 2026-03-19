from tasks import add_task, load_tasks, toggle_task, edit_task

def display_menu():
    print("\n--- PhexTech Task Manager ---")
    print("1. Load Tasks")
    print("2. Add Task")
    print("3. Edit Task")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            show_tasks_list() # moved to helper function for consistent display across app
                
        elif choice == '2':
            desc = input("Enter task description: ")
            add_task(desc)
            print("Task added.")
            
        elif choice == '3':
            tasks = load_tasks()
            if not show_tasks_list():
                continue # if no tasks, skip edit flow
                
            try:
                idx = int(input("Enter task number to edit: "))
                current_desc = tasks[idx - 1]['description']
                print(f"Current description: {current_desc}")
                
                new_desc = input("Enter new description (or press enter to cancel): ")

                if new_desc.strip():
                    if edit_task(idx, new_desc):
                        print("Task successfully updated.")
                    else:
                        print("Failed to update task. Please try again.")
                else:
                    print("Edit cancelled.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid task number.")
            
        elif choice == '4':
            print("Thank you for using PhexTech Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
# refactoring edit_task to return a boolean for success/failure
def show_tasks_list():
    """Helper function to display tasks consistently across app"""
    tasks = load_tasks()
    if not tasks:
        print("\n--- No tasks found. Please add a task first. ---")
        return False
    
    print("\n--- Current Tasks ---")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task['completed'] else "❌"
        print(f"{i}. {task['description']} [{status}]")
    return True
if __name__ == "__main__":
    main()