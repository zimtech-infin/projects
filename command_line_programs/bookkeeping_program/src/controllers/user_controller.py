# src/controllers/user_controller.py

from models.user import User, Session

class UserController:
    """Controller to manage user-related operations."""

    def __init__(self):
        self.session = Session()

    def create_user(self, name, role, contact_info):
        """Create a new user."""
        user = User(name=name, role=role, contact_info=contact_info)
        user.add_user(self.session)
        return user

    def delete_user(self, user_id):
        """Delete a user."""
        user = User.get_user_by_id(self.session, user_id)
        if user:
            user.remove_user(self.session)
            return True
        return False

    def update_user(self, user_id, name=None, role=None, contact_info=None):
        """Update an existing user."""
        user = User.get_user_by_id(self.session, user_id)
        if user:
            user.update_user(self.session, name=name, role=role, contact_info=contact_info)
            return True
        return False

    def get_user_by_id(self, user_id):
        """Retrieve a user by their ID."""
        return User.get_user_by_id(self.session, user_id)
