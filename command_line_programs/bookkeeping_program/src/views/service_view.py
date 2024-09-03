# src/views/service_view.py

import sys
import os

# Adjust the path to ensure imports work correctly when running the file directly
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, '..'))

# Importing the ServiceController from the controllers module
from controllers.service_controller import ServiceController

class ServiceView:
    """View to interact with service operations in the system."""

    def __init__(self):
        self.service_controller = ServiceController()

    def display_service_info(self, service_id):
        """Display service information by ID."""
        service = self.service_controller.get_service_by_id(service_id)
        if service:
            print(f"Service ID: {service.service_id}, Type: {service.type}, Date: {service.date}, Client ID: {service.client_id}")
        else:
            print(f"No service found with ID: {service_id}")

    def add_service_form(self):
        """Simulate a form to add a new service."""
        service_type = input("Enter service type: ")
        service_date = input("Enter service date (YYYY-MM-DD): ")
        client_id = int(input("Enter client ID for the service: "))
        self.service_controller.add_service(type=service_type, date=service_date, client_id=client_id)
        print("Service added successfully.")

    def delete_service_form(self):
        """Simulate a form to delete a service."""
        service_id = int(input("Enter service ID to delete: "))
        if self.service_controller.delete_service(service_id):
            print("Service deleted successfully.")
        else:
            print("Service not found.")

    def update_service_form(self):
        """Simulate a form to update a service."""
        service_id = int(input("Enter service ID to update: "))
        service_type = input("Enter new service type (leave blank to keep current): ")
        service_date = input("Enter new service date (leave blank to keep current, format: YYYY-MM-DD): ")
        client_id = input("Enter new client ID for the service (leave blank to keep current): ")
        self.service_controller.update_service(service_id, type=service_type, date=service_date, client_id=client_id)
        print("Service updated successfully.")

# Entry point for the script
if __name__ == "__main__":
    service_view = ServiceView()
    service_view.add_service_form()  # Example action
