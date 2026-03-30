import datetime

class TodoList:
    def __init__(self):
        self.task = []
    
    def addTask(self, taskName):
        task = {"name": taskName, "done": False}
        self.task.append(task)

    def list_tasks(self):
        for id, task in enumerate(self.task):
            status = "✔️" if task["done"] else "❌"
            print(f"{id} - {task['name']} [{status}]")
        
    def remove_task(self, id):
        if 0 <= id < len(self.task):
            self.task.pop(id)
        else:
            print("Geçersiz index!")

    def complete_task(self, id):
        if 0 <= id < len(self.task):
            self.task[id]["done"] = True
        else:
            print("Geçersiz index!")

# --- Test ---
toDo = TodoList()
toDo.addTask("Ödev yap")
toDo.addTask("Alışveriş")

print("Başlangıç:")
toDo.list_tasks()

toDo.complete_task(1)

print("\nTamamlandıktan sonra:")
toDo.list_tasks()