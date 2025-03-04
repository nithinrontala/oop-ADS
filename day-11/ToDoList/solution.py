class Task:
    def __init__(self, task_id, title, description, due_date, priority):
        self.task_id = int(task_id)
        self.title = title.strip().strip('"')
        self.description = description.strip().strip('"')
        self.due = due_date.strip().strip('"')
        self.priority = priority.strip().strip('"')
        self.is_completed = False

    def mark_completed(self):
        self.is_completed = True

    def update_task(self, title, description, due_date, priority):
        self.title = title.strip().strip('"')
        self.description = description.strip().strip('"')
        self.due = due_date.strip().strip('"')
        self.priority = priority.strip().strip('"')
    
    def get_task_details(self):
        if self.is_completed:
            status = "[Completed]" 
        else:
            status = "[Pending]"
        return f"{self.task_id}. {status} {self.title} - Due: {self.due}, Priority: {self.priority}" 

class ToDoList:
    def __init__(self):
        self.details = []
    
    def add_task(self, task):
        task = task.split(",")
        t = Task(task[0], task[1], task[2], task[3], task[4])
        self.details.append(t)

    def remove_task(self, task_id):
        task_id = int(task_id)
        self.details = [task for task in self.details if task.task_id != task_id]
    
    def get_all_tasks(self):
        print("All Tasks:")
        for task in self.details:
            print(task.get_task_details())
    
    def get_pending_tasks(self):
        print("Pending Tasks:")
        for task in self.details:
            if not task.is_completed:
                print(task.get_task_details())
    
    def get_completed_tasks(self):
        print("Completed Tasks:")
        for task in self.details:
            if task.is_completed:
                print(task.get_task_details())
    
    def sort_tasks(self, by):
        if by == "due_date":
            self.details.sort(key=lambda task: task.due)
        elif by == "priority":
            priority_order = {"High": 1, "Medium": 2, "Low": 3}
            self.details.sort(key=lambda task: priority_order.get(task.priority, 4))
    
    def search_tasks(self, keyword):
        for task in self.details:
            if keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower():
                print(task.get_task_details())

    def mark_complete(self, task_id):
        task_id = int(task_id)
        for task in self.details:
            if task.task_id == task_id:
                task.mark_completed()
                break

def main():
    todo = ToDoList()
    while True:
        try:
            s = input().strip(")")
            s = s.split("(")
            command = s[0]
            args = s[1] if len(s) > 1 else ""
            
            if command == "add_task":
                todo.add_task(args)
            elif command == "get_all_tasks":
                todo.get_all_tasks()
            elif command == "mark_completed":
                todo.mark_complete(args)
            elif command == "get_completed_tasks":
                todo.get_completed_tasks()
            elif command == "get_pending_tasks":
                todo.get_pending_tasks()
            elif command == "remove_task":
                todo.remove_task(args)
            elif command == "sort_tasks":
                todo.sort_tasks(args)
            elif command == "search_tasks":
                todo.search_tasks(args)
            
        except:
            break

if __name__ == "__main__":
    main()