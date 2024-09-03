# src/views/client_view.py

import sys
import os

# Adjust the path to ensure imports work correctly when running the file directly
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, '..'))

# Importing the ClientController from the controllers module
from controllers.client_controller import ClientController

class ClientView:
    """View to interact with client operations in the system."""

    def __init__(self):
        self.client_controller = ClientController()

    def display_client_info(self, client_id):
        """Display client information by ID."""
        client = self.client_controller.get_client_by_id(client_id)
        if client:
            print(f"Client ID: {client.client_id}, Name: {client.name}, Contact Info: {client.contact_info}, Service History: {client.service_history}")
        else:
            print(f"No client found with ID: {client_id}")

    def create_client_form(self):
        """Simulate a form to create a new client."""
        name = input("Enter client name: ")
        contact_info = input("Enter client contact info: ")
        self.client_controller.create_client(name=name, contact_info=contact_info)
        print("Client created successfully.")

    def delete_client_form(self):
        """Simulate a form to delete a client."""
        client_id = int(input("Enter client ID to delete: "))
        if self.client_controller.delete_client(client_id):
            print("Client deleted successfully.")
        else:
            print("Client not found.")

    def update_client_form(self):
        """Simulate a form to update a client."""
        client_id = int(input("Enter client ID to update: "))
        name = input("Enter new client name (leave blank to keep current): ")
        contact_info = input("Enter new client contact info (leave blank to keep current): ")
        self.client_controller.update_client(client_id, name=name, contact_info=contact_info)
        print("Client updated successfully.")

# Entry point for the script
if __name__ == "__main__":
    client_view = ClientView()
    client_view.create_client_form()  # Example action
