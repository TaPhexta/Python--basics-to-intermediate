from tasks import add_task, load_tasks

def display_menu():
    print("\n--- Task Manager ---")
    print("1. Add Task")
    print("2. Load Tasks")
    print("3. Exit")
    
def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            tasks = load_tasks()
            if not tasks:
                print("No tasks found. Please add a task first.")
            for i, task in enumerate(tasks, 1):
                status = "✅" if task['completed'] else "❌"
                print(f"{i}. {task['title']} [{status}]")
                
        elif choice == '2':
            desc = input("Enter task description: ")
            add_task(desc)
            print("Task added.")
            
        elif choice == '3':
            print("Thank you for using PhexTech Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()