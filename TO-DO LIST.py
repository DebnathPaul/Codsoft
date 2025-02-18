

import datetime

class Task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"[{status}] {self.title} (Due: {self.due_date}, Priority: {self.priority})"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add(self, title, description, due_date, priority):
        task = Task(title, description, due_date, priority)
        self.tasks.append(task)
        print(f"Task '{title}' added.")

    def view(self):
        print("Your task list")
        if not self.tasks:
            print("No tasks available.")
        for task in self.tasks:
            print(task)

    def update(self, title, new_title, new_description, new_due_date, new_priority):
        view(self)
        for task in self.tasks:
            if task.title == title:
                task.title = new_title
                task.description = new_description
                task.due_date = new_due_date
                task.priority = new_priority
                print(f"Task '{title}' updated.")
                return
        print(f"Task '{title}' not found.")
        view(self)

    def delete(self, title):
        view(self)
        
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Task '{title}' deleted.")
                return
        print(f"Task '{title}' not found.")
        view(self)

    def task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.completed = True
                print(f"Task '{title}' marked as completed.")
                return
        print(f"Task '{title}' not found.")

def ABCD():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List:")
        print("Press '1' for Add Task")
        print("Press '2' for View Tasks")
        print("Press '3' for Update Task")
        print("Press '4' for Delete Task")
        print("Press '5' for Mark Task as Completed")
        print("Press '6' for Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due Date (YYYY-MM-DD): ")
            priority = input("Priority (Low/Medium/High): ")
            todo_list.add(title, description, due_date, priority)
        elif choice == "2":
            todo_list.view()
        elif choice == "3":
            title = input("Enter the title of the task to update: ")
            new_title = input("New Title: ")
            new_description = input("New Description: ")
            new_due_date = input("New Due Date (YYYY-MM-DD): ")
            new_priority = input("New Priority (Low/Medium/High): ")
            todo_list.update(title, new_title, new_description, new_due_date, new_priority)
        elif choice == "4":
            title = input("Enter the title of the task to delete: ")
            todo_list.delete(title)
        elif choice == "5":
            title = input("Enter the title of the task to mark as completed: ")
            todo_list.task_completed(title)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


ABCD()
