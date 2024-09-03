# src/controllers/service_controller.py

from models.service import Service, Session

class ServiceController:
    """Controller to manage service-related operations."""

    def __init__(self):
        self.session = Session()

    def add_service(self, type, date, client_id):
        """Add a new service to a client's history."""
        service = Service(type=type, date=date, client_id=client_id)
        service.add_service(self.session)
        return service

    def delete_service(self, service_id):
        """Delete a service from the system."""
        service = Service.get_service_by_id(self.session, service_id)
        if service:
            service.remove_service(self.session)
            return True
        return False

    def update_service(self, service_id, type=None, date=None, client_id=None):
        """Update an existing service."""
        service = Service.get_service_by_id(self.session, service_id)
        if service:
            service.update_service(self.session, type=type, date=date, client_id=client_id)
            return True
        return False

    def get_service_by_id(self, service_id):
        """Retrieve a service by its ID."""
        return Service.get_service_by_id(self.session, service_id)
