def add_task(todo_list):
    task = input("Enter the task to add: ")
    todo_list[len(todo_list) + 1] = task
    print("Task added successfully!")

def delete_task(todo_list):
    task_number = int(input("Enter the task number to delete: "))
    if task_number in todo_list:
        del todo_list[task_number]
        print("Task deleted successfully!")
    else:
        print("Task not found!")

def display_tasks(todo_list):
    if todo_list:
        print("To-Do List:")
        for task_number, task in todo_list.items():
            print(f"{task_number}. {task}")
    else:
        print("To-Do List is empty!")

def todo_list_app():
    todo_list = {}
    while True:
        print("\n1. Add Task\n2. Delete Task\n3. Display Tasks\n4. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            delete_task(todo_list)
        elif choice == '3':
            display_tasks(todo_list)
        elif choice == '4':
            print("Thank you for using the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    todo_list_app()
