# class Task:
#     def __init__(self, task_id, title, description, due_date, priority):
#         self.task_id = task_id
#         self.title = title
#         self.description = description
#         self.due_date = due_date
#         self.priority = priority
#         self.is_completed = False

#     def mark_completed(self):
#         """Marks the task as completed."""
#         self.is_completed = True

#     def update_task(self, title, description, due_date, priority):
#         """Updates task properties."""
#         self.title = title
#         self.description = description
#         self.due_date = due_date
#         self.priority = priority

#     def get_task_details(self):
#         """Returns a formatted string with task details."""
#         status = "Completed" if self.is_completed else "Pending"
#         return f"[{status}] {self.title} - Due: {self.due_date}, Priority: {self.priority}"


# class ToDoList:
#     def __init__(self):
#         self.tasks = []

#     def add_task(self, task: Task):
#         """Adds a new task to the list."""
#         self.tasks.append(task)

#     def remove_task(self, task_id: int):
#         """Removes a task using its task_id."""
#         self.tasks = [task for task in self.tasks if task.task_id != task_id]

#     def get_all_tasks(self):
#         """Returns all tasks in a formatted way."""
#         return [task.get_task_details() for task in self.tasks]

#     def get_pending_tasks(self):
#         """Returns only incomplete tasks."""
#         return [task.get_task_details() for task in self.tasks if not task.is_completed]

#     def get_completed_tasks(self):
#         """Returns only completed tasks."""
#         return [task.get_task_details() for task in self.tasks if task.is_completed]

#     def sort_tasks(self, by="due_date"):
#         """Sorts tasks based on the chosen attribute (due_date or priority)."""
#         if by == "due_date":
#             self.tasks.sort(key=lambda x: x.due_date)
#         elif by == "priority":
#             priority_order = {"High": 1, "Medium": 2, "Low": 3}
#             self.tasks.sort(key=lambda x: priority_order.get(x.priority, 4))

#     def search_tasks(self, keyword: str):
#         """Searches for tasks containing the keyword in the title or description."""
#         return [task.get_task_details() for task in self.tasks if keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower()]


# # Example Usage (Test Cases)

# # Create a To-Do List
# todo = ToDoList()

# # Create Task Instances
# task1 = Task(1, "Submit Report", "Complete project report by Friday", "2025-02-02", "High")
# task2 = Task(2, "Grocery Shopping", "Buy fruits and vegetables", "2025-02-04", "Medium")
# task3 = Task(3, "Workout", "Morning jogging for 30 minutes", "2025-02-01", "Low")

# # Add tasks to To-Do List
# todo.add_task(task1)
# todo.add_task(task2)
# todo.add_task(task3)

# # Display all tasks
# print("All Tasks:")
# for task in todo.get_all_tasks():
#     print(task)

# # Mark task1 as completed
# task1.mark_completed()

# # Display completed tasks
# print("\nCompleted Tasks:")
# for task in todo.get_completed_tasks():
#     print(task)

# # Sort tasks by due date
# todo.sort_tasks(by="due_date")
# print("\nSorted by Due Date:")
# for task in todo.get_all_tasks():
#     print(task)

# # Search for tasks with the keyword "Workout"
# print("\nSearch for 'Workout':")
# for task in todo.search_tasks("Workout"):
#     print(task)

# # Remove task with ID 2
# todo.remove_task(2)

# # Display remaining tasks
# print("\nRemaining Tasks After Removing Task with ID 2:")
# for task in todo.get_all_tasks():
#     print(task)


class Task:
    def __init__(self, task_id, title, description, due_date, priority):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.is_completed = False

    def mark_completed(self):
        """Marks the task as completed."""
        self.is_completed = True

    def update_task(self, title, description, due_date, priority):
        """Updates task properties."""
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority

    def get_task_details(self):
        """Returns a formatted string with task details."""
        status = "Completed" if self.is_completed else "Pending"
        return f"[{status}] {self.title} - Due: {self.due_date}, Priority: {self.priority}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        """Adds a new task to the list."""
        self.tasks.append(task)

    def remove_task(self, task_id: int):
        """Removes a task using its task_id."""
        new_tasks = []
        for task in self.tasks:
            if task.task_id != task_id:
                new_tasks.append(task)
        self.tasks = new_tasks

    def get_all_tasks(self):
        """Returns all tasks in a formatted way."""
        task_details = []
        for task in self.tasks:
            task_details.append(task.get_task_details())
        return task_details

    def get_pending_tasks(self):
        """Returns only incomplete tasks."""
        pending_tasks = []
        for task in self.tasks:
            if not task.is_completed:
                pending_tasks.append(task.get_task_details())
        return pending_tasks

    def get_completed_tasks(self):
        """Returns only completed tasks."""
        completed_tasks = []
        for task in self.tasks:
            if task.is_completed:
                completed_tasks.append(task.get_task_details())
        return completed_tasks

    def sort_tasks(self, by="due_date"):
        """Sorts tasks based on the chosen attribute (due_date or priority)."""
        if by == "due_date":
            self.tasks.sort(key=lambda x: x.due_date)
        elif by == "priority":
            priority_order = {"High": 1, "Medium": 2, "Low": 3}
            self.tasks.sort(key=lambda x: priority_order.get(x.priority, 4))

    def search_tasks(self, keyword: str):
        """Searches for tasks containing the keyword in the title or description."""
        search_results = []
        for task in self.tasks:
            if keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower():
                search_results.append(task.get_task_details())
        return search_results


# Example Usage (Test Cases)

# Create a To-Do List
todo = ToDoList()

# Create Task Instances
task1 = Task(1, "Submit Report", "Complete project report by Friday", "2025-02-02", "High")
task2 = Task(2, "Grocery Shopping", "Buy fruits and vegetables", "2025-02-04", "Medium")
task3 = Task(3, "Workout", "Morning jogging for 30 minutes", "2025-02-01", "Low")

# Add tasks to To-Do List
todo.add_task(task1)
todo.add_task(task2)
todo.add_task(task3)

# Display all tasks
print("All Tasks:")
all_tasks = todo.get_all_tasks()
for task in all_tasks:
    print(task)

# Mark task1 as completed
task1.mark_completed()

# Display completed tasks
print("\nCompleted Tasks:")
completed_tasks = todo.get_completed_tasks()
for task in completed_tasks:
    print(task)

# Sort tasks by due date
todo.sort_tasks(by="due_date")
print("\nSorted by Due Date:")
sorted_tasks = todo.get_all_tasks()
for task in sorted_tasks:
    print(task)

# Search for tasks with the keyword "Workout"
print("\nSearch for 'Workout':")
searched_tasks = todo.search_tasks("Workout")
for task in searched_tasks:
    print(task)

# Remove task with ID 2
todo.remove_task(2)

# Display remaining tasks
print("\nRemaining Tasks After Removing Task with ID 2:")
remaining_tasks = todo.get_all_tasks()
for task in remaining_tasks:
    print(task)
