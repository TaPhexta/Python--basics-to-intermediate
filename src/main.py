from tasks import (
    delete_task, generate_username, create_profile, authenticate, get_user_tasks, add_task, toggle_task, edit_task, is_valid_pin
)

def show_tasks(username):
    """Display the user's tasks."""
    tasks = get_user_tasks(username)
    print(f"\n--- {username}'s Tasks ---")
    if not tasks:
        print("No tasks found.")
        return False
    
    for i, task in enumerate(tasks, 1):
        status = "✅" if task['completed'] else "❌"
        print(f"{i}. {task['description']} [{status}]")
    return True


def main():
    while True:
        print("\n--- PhexTech Task Manager ---")
        print("1. Login")
        print("2. Register New Profile")
        print("3. Exit")

        choice = input("Choose an option: ")
        
        if choice == '1':
            user = input("Enter username: ").lower().strip()
            pin = input("Enter PIN: ").strip()
            
            if authenticate(user, pin):
                print(f"\nWelcome back, {user}!")
                
                # --- Auth'd user session ---
                while True:
                    print(f"\n--- {user}'s Dashboard ---")
                    print("1. View Status")
                    print("2. Add Task")
                    print("3. Edit Task")
                    print("4. Delete task")
                    print("5. Logout")
                    
                    sub_choice = input("Choose an option: ")
                    
                    if sub_choice == '1':
                       if show_tasks(user):
                            idx =input("\nEnter number to toggle (or Enter to go back):")
                            if idx.isdigit():
                                toggle_task(user, int(idx))
                    
                    elif sub_choice == '2':
                        desc = input("Enter task description: ")
                        add_task(user, desc)
                        print("Task added.")
                        
                    elif sub_choice == '3':
                        if show_tasks(user):
                            try:
                                idx = input("\nEnter number to edit (or Enter to go back): ")
                                if idx.isdigit():
                                    new_desc = input("Enter new description: ")
                                    if edit_task(user, int(idx), new_desc):
                                        print("Task updated.")
                            except ValueError:
                                    print("Invalid input.")
                    elif sub_choice == '4':
                        if show_tasks(user):
                            try:
                                idx = input("\nEnter number to delete (or Enter to go back): ")
                                if idx.isdigit():
                                    if delete_task(user, int(idx)):
                                        print("Task deleted.")
                            except ValueError:
                                    print("Invalid input.")
                                    
                    elif sub_choice == '5':
                        break
            else:
                print("Invalid Username or PIN. Please try again.")
                    
        elif choice == '2':
            # --- Registration Flow ---
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            option = generate_username(first_name, last_name)
            
            print("\nChoose a Username:")
            print(f"1. {option[0]}")
            print(f"2. {option[1]}")
            
            u_choice = input("Select an option: ")
            chosen_user = option[0] if u_choice == '1' else option[1]
            
            # PIN creation with validation
            while True:
                new_pin = input("Create a 6-digit PIN (max 3 repeating digits): ")
                if is_valid_pin(new_pin):
                    create_profile(chosen_user, new_pin)
                    print(f"Profile created for {chosen_user}. You can now log in.")
                    print(f"Your username is: {chosen_user}")
                    break
                else:
                    print("Invalid PIN. Must be 6 digits with no more than 3 of the same number.")
            
        elif choice =='3':
            print("Thank you for using PhexTech Task Manager!")
            print("Goodbye!")
            break
                
if __name__ == "__main__":
    main()