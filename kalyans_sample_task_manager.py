class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"Title: {self.title}\nDescription: {self.description}\nStatus: {status}"
    # The Task class is defined. This class represents an individual task. It has three attributes: title, description, and completed.
    # The __init__ method is the constructor for the Task class. It initializes the attributes title and description based on #the provided parameters. The completed attribute is set to False by default.
    # The mark_completed method is used to mark a task as completed by setting the completed attribute to True.
    # The __str__ method is a special method that provides a string representation of a Task object. It returns a formatted #string containing the task's title, description, and completion status.
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            print(f"Task {index}:\n{task}\n")

    def mark_task_completed(self, task_number):
        if 1<= task_number <=len(self.tasks):
            task = self.tasks[task_number - 1]
            task.mark_completed()
            print("Hay Kalyan your Task marked as completed")
        else:
            print("Hay kalyan please give me the valid task number")

    def delete_task(self, task_number):
        if 1<=task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            print("Hay kalyan your task is deleted")
        else:
            print("Hay kalyan please give me the valid task number")

    # The TaskManager class is defined. This class manages a collection of tasks.
    # The __init__ method initializes an empty list tasks to store tasks managed by the TaskManager.
    # The add_task method takes a Task object as a parameter and appends it to the tasks list.
    # The list_tasks method iterates through the tasks list, displaying each task's details using the __str__ method.
    # The mark_task_completed method marks a task as completed based on the provided task number. It checks if the task number is within a valid range and then calls the mark_completed method of the corresponding Task object.
    # The delete_task method deletes a task based on the provided task number. It checks if the task number is within a valid range and removes the corresponding Task object from the tasks list.

def main():
    task_manager = TaskManager()

    while True:
        print("Kalyan's Simple Task Manager")
        print("1. Add Task")
        print("2. List of Tasks")
        print("3. Mark my Task as Complete")
        print("4. Delete Task")
        print("0. Exit")

        choice = input("Enter your choice Mr.Kalyan: ")

        if choice =="0":
            print("Exiting kalyan's Task Manager")
            break
        elif choice == "1":
            title = input("Enter your task title: ")
            description = input("Enter your task description: ")
            task = Task(title, description)
            task_manager.add_task(task)
            print("Task Added")
        elif choice == "2":
            task_manager.list_tasks()
        elif choice == "3":
            task_manager.list_tasks()
            task_number= int(input("choose the that you want to mark as complete: "))
            task_manager.mark_task_completed(task_number)
        elif choice == "4":
            task_manager.list_tasks()
            task_number = int(input("choose the that you want to mark as complete: "))
            task_manager.delete_task(task_number)
        else:
            print("Invalid choice. please select the valid option: ")

if __name__ == "__main__":
    main()
