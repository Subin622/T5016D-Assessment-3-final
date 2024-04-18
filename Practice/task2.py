# task.py

class Task:
    def __init__(self, name="", description="", completed=False):
        self.name = name
        self.description = description
        self.completed = completed

    def __str__(self):
        return f"Task: {self.name}\nDescription: {self.description}\nCompleted: {self.completed}\n"

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def get_completed_tasks(self):
        return [task for task in self.tasks if task.completed]

def main():
    todo_list = TodoList()

    # Adding tasks
    todo_list.add_task(Task("Buy groceries", "Milk, eggs, bread"))
    todo_list.add_task(Task("Finish project", "Complete the coding project"))

    # Marking a task as complete
    todo_list.mark_task_complete("Buy groceries")

    # Display pending and completed tasks
    print("Pending Tasks:")
    for task in todo_list.get_pending_tasks():
        print(task)
        print("----------------")

    print("Completed Tasks:")
    for task in todo_list.get_completed_tasks():
        print(task)
        print("----------------")

if __name__ == "__main__":
    main()

