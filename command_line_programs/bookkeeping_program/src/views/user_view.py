# src/views/user_view.py

import sys
import os

# Adjust the path to ensure imports work correctly when running the file directly
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, '..'))

# Importing the UserController from the controllers module
from controllers.user_controller import UserController

class UserView:
    """View to interact with user operations in the system."""

    def __init__(self):
        self.user_controller = UserController()

    def display_user_info(self, user_id):
        """Display user information by ID."""
        user = self.user_controller.get_user_by_id(user_id)
        if user:
            print(f"User ID: {user.user_id}, Name: {user.name}, Role: {user.role}, Contact Info: {user.contact_info}")
        else:
            print(f"No user found with ID: {user_id}")

    def create_user_form(self):
        """Simulate a form to create a new user."""
        name = input("Enter user name: ")
        role = input("Enter user role: ")
        contact_info = input("Enter user contact info: ")
        self.user_controller.create_user(name=name, role=role, contact_info=contact_info)
        print("User created successfully.")

    def delete_user_form(self):
        """Simulate a form to delete a user."""
        user_id = int(input("Enter user ID to delete: "))
        if self.user_controller.delete_user(user_id):
            print("User deleted successfully.")
        else:
            print("User not found.")

    def update_user_form(self):
        """Simulate a form to update a user."""
        user_id = int(input("Enter user ID to update: "))
        name = input("Enter new user name (leave blank to keep current): ")
        role = input("Enter new user role (leave blank to keep current): ")
        contact_info = input("Enter new user contact info (leave blank to keep current): ")
        self.user_controller.update_user(user_id, name=name, role=role, contact_info=contact_info)
        print("User updated successfully.")

# Entry point for the script
if __name__ == "__main__":
    user_view = UserView()
    user_view.create_user_form()  # Example action
