class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_task(self, task, status="todo"):
        self.model.add_task(task, status)
        self.view.update_summary()

    def update_task(self, task, new_status):
        self.model.update_task(task, new_status)
        self.view.update_summary()

    def delete_task(self, task):
        self.model.delete_task(task)
        self.view.update_summary()