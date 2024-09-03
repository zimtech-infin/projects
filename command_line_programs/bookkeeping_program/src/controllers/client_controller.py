# src/controllers/client_controller.py

from models.client import Client, Session

class ClientController:
    """Controller to manage client-related operations."""

    def __init__(self):
        self.session = Session()

    def create_client(self, name, contact_info, service_history=None):
        """Create a new client."""
        client = Client(name=name, contact_info=contact_info, service_history=service_history)
        client.add_client(self.session)
        return client

    def delete_client(self, client_id):
        """Delete a client."""
        client = Client.get_client_by_id(self.session, client_id)
        if client:
            client.remove_client(self.session)
            return True
        return False

    def update_client(self, client_id, name=None, contact_info=None, service_history=None):
        """Update an existing client."""
        client = Client.get_client_by_id(self.session, client_id)
        if client:
            client.update_client(self.session, name=name, contact_info=contact_info, service_history=service_history)
            return True
        return False

    def get_client_by_id(self, client_id):
        """Retrieve a client by their ID."""
        return Client.get_client_by_id(self.session, client_id)
