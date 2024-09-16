# Command-Line To-Do List Application

def display_menu():
    print("\n--- To-Do List Application ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\n--- To-Do List ---")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def update_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter the task number to update: "))
        if 1 <= task_num <= len(tasks):
            new_task = input("Enter the updated task: ")
            tasks[task_num - 1] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
