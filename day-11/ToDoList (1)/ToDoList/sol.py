class Task:
    def __init__(self, task_id, title, description, due_date, priority):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def update_task(self, task_id, title, description, due_date, priority):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority

    def get_task_info(self):
        if self.completed :
            status = "Completed" 
        else:
            status = "Pending"
        return f"{self.task_id}. [{status}] {self.title} - Due: {self.due_date}, Priority: {self.priority}"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_details):
        task_id, title, description, due_date, priority = map(str, task_details)
        t =Task(task_id, title, description, due_date, priority)
        self.tasks.append(t)

    def remove_task(self, task_id):
        after_removing = []
        for task in self.tasks:
            if task.task_id != str(task_id):
                after_removing.append(task)
        self.tasks = after_removing

    def get_all_tasks(self):
        all_tasks = []
        for task in self.tasks:
            all_tasks.append(task.get_task_info())
        return all_tasks

    def get_pending_tasks(self):
        pending_tasks = []
        for task in self.tasks:
            if not task.completed:
                pending_tasks.append(task.get_task_info())
        return pending_tasks

    def get_completed_tasks(self):
        completed_tasks = []
        for task in self.tasks:
            if task.completed:
                completed_tasks.append(task.get_task_info())
        return completed_tasks

    def sort_tasks(self, by):
        if by == "due_date":
            self.tasks.sort(key=lambda task: task.due_date)
        elif by == "priority":
            self.tasks.sort(key=lambda task: task.priority)

    def search_tasks(self, keyword):
        word = keyword.lower()
        searched = []
        for task in self.tasks:
            if word in task.title.lower() or word in task.description.lower():
                searched.append(task.get_task_info())
        return searched


def manage_todo_list():
    todo = TodoList()

    while True:
        try:
            s = input().strip()

            if s.startswith("add_task"):
                task_details = eval(s.split("add_task")[1])
                todo.add_task(task_details)

            elif s.startswith("update_task"):
                task_details = eval(s.split("update_task")[1])
                for task in todo.tasks:
                    if task.task_id == str(task_details[0]):
                        task.update_task(*task_details)

            elif s.startswith("get_all_tasks"):
                all_tasks = todo.get_all_tasks()
                print("All Tasks:")
                for task in all_tasks:
                    print(task)
                print()

            elif s.startswith("get_completed_tasks"):
                completed_tasks = todo.get_completed_tasks()
                print("Completed Tasks:")
                for task in completed_tasks:
                    print(task)
                print()

            elif s.startswith("get_pending_tasks"):
                pending_tasks = todo.get_pending_tasks()
                print("Pending Tasks:")
                for task in pending_tasks:
                    print(task)
                print()

            elif s.startswith("mark_completed"):
                task_id = int(eval(s.split("mark_completed")[1]))
                for task in todo.tasks:
                    if task.task_id == str(task_id):
                        task.mark_as_completed()

            elif s.startswith("remove_task"):
                task_id = eval(s.split("remove_task")[1])
                todo.remove_task(task_id)

            elif s.startswith("sort_tasks"):
                criteria = eval(s.split("sort_tasks")[1])
                todo.sort_tasks(criteria)
                sorted_tasks = todo.get_all_tasks()
                print("All Tasks:")
                for task in sorted_tasks:
                    print(task)
                print()

            elif s.startswith("search_tasks"):
                word = eval(s.split("search_tasks")[1])
                print(f"Search Results for: {word}")
                search_results = todo.search_tasks(word)
                for result in search_results:
                    print(result)
                print()

        except EOFError:
            break


if __name__ == "__main__":
    manage_todo_list()
