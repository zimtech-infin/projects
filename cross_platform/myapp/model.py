class User:
    def __init__(self, first_name, last_name, email, title, password, role='user'):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.title = title
        self.password = password
        self.role = role
        self.notes = []
        self.kanban = {
            "todo": [],
            "in_progress": [],
            "roadblock": [],
            "complete": []
        }

    def add_task(self, task, status="todo"):
        self.kanban[status].append(task)

    def update_task(self, task, new_status):
        for status in self.kanban:
            if task in self.kanban[status]:
                self.kanban[status].remove(task)
                self.kanban[new_status].append(task)
                break

    def delete_task(self, task):
        for status in self.kanban:
            if task in self.kanban[status]:
                self.kanban[status].remove(task)
                break

    def get_summary(self):
        return {
            "total_tasks": sum(len(tasks) for tasks in self.kanban.values()),
            "milestones": len(self.notes),
            "roadblocks": len(self.kanban["roadblock"])
        }

class UserManager:
    def __init__(self):
        self.users = {}
        self.credentials = {}

    def create_user(self, first_name, last_name, email, title, password, role='user'):
        if email in self.users:
            raise ValueError("User already exists")
        user = User(first_name, last_name, email, title, password, role)
        self.users[email] = user
        self.credentials[email] = password
        return user

    def get_user(self, email):
        return self.users.get(email)

    def validate_user(self, email, password):
        return self.credentials.get(email) == password

    def change_password(self, email, new_password):
        if email in self.users:
            self.users[email].password = new_password
            self.credentials[email] = new_password

    def assign_role(self, email, role):
        if email in self.users:
            self.users[email].role = role