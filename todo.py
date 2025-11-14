import os

# --- Constants ---
TASK_FILE = "tasks.txt"
HEART_DECO = "🌸"
CHECK_MARK = "✅"
CROSS_MARK = "❌"
LIST_ICON = "📝"
WAVE_ICON = "👋"

# --- Functions ---

def load_tasks():
    """Loads tasks from the task file. Creates the file if it doesn't exist."""
    tasks = []
    try:
        with open(TASK_FILE, 'r') as f:
            # .strip() removes the newline character ('\n') from each line
            tasks = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        # If the file doesn't exist, create it
        with open(TASK_FILE, 'w') as f:
            pass  # Just create an empty file
    return tasks

def save_tasks(tasks):
    """Saves the current list of tasks to the task file."""
    with open(TASK_FILE, 'w') as f:
        for task in tasks:
            f.write(task + '\n')  # Add a newline for each task

def show_menu():
    """Prints the 'cute' main menu."""
    print("\n" + HEART_DECO * 25)
    print(f"{HEART_DECO}       MY TO-DO LIST APP       {HEART_DECO}")
    print(HEART_DECO * 25)
    print("  1. View All Tasks")
    print("  2. Add a New Task")
    print("  3. Remove a Task")
    print("  4. Quit")
    print(HEART_DECO * 25)

def view_tasks(tasks):
    """Prints the current list of tasks."""
    print(f"\n--- {LIST_ICON} Your To-Do List ---")
    if not tasks:
        print("✨ Your list is empty! Time to add something. ✨")
    else:
        # enumerate adds a counter (starting from 1)
        for i, task in enumerate(tasks, 1):
            print(f"  {i}. {task}")
    print("----------------------------\n")

def add_task(tasks):
    """Adds a new task to the list and saves."""
    task = input("Enter your new task: ")
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"\n{CHECK_MARK} Task '{task}' added successfully!")
    else:
        print(f"\n{CROSS_MARK} Task cannot be empty.")

def remove_task(tasks):
    """Removes a task from the list by its number."""
    view_tasks(tasks)  # Show tasks first so user knows what to remove
    
    if not tasks:
        return  # Nothing to remove

    try:
        num_to_remove = int(input("Enter the number of the task to remove: "))
        
        # Check if the number is valid
        if 1 <= num_to_remove <= len(tasks):
            # .pop() removes the item at that index (index is num - 1)
            removed_task = tasks.pop(num_to_remove - 1)
            save_tasks(tasks)
            print(f"\n{CHECK_MARK} Task '{removed_task}' removed successfully!")
        else:
            print(f"\n{CROSS_MARK} Invalid number! Please enter a number from the list.")
    except ValueError:
        print(f"\n{CROSS_MARK} Invalid input! Please enter a number.")

# --- Main Application Loop ---
def main():
    tasks = load_tasks()  # Load tasks when the app starts

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print(f"\nGoodbye! Keep up the great work! {WAVE_ICON}")
            break
        else:
            print(f"\n{CROSS_MARK} Invalid choice. Please pick 1, 2, 3, or 4.")

# Run the app
if __name__ == "__main__":
    main()
  
