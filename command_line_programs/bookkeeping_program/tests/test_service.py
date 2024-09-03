# tests/test_service.py

import unittest
from models.service import Service, Session
from datetime import date

class TestService(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.session = Session()
        # Create a sample service object for testing
        self.service = Service(type="Cleaning", date=date(2024, 9, 1), client_id=1)
        self.service.add_service(self.session)

    def tearDown(self):
        """Clean up test fixtures after each test method."""
        self.session.query(Service).delete()  # Delete all entries in the Service table
        self.session.commit()
        self.session.close()

    def test_add_service(self):
        """Test adding a service."""
        service = Service.get_service_by_id(self.session, self.service.service_id)
        self.assertIsNotNone(service)
        self.assertEqual(service.type, "Cleaning")
        self.assertEqual(service.client_id, 1)

    def test_remove_service(self):
        """Test removing a service."""
        self.service.remove_service(self.session)
        service = Service.get_service_by_id(self.session, self.service.service_id)
        self.assertIsNone(service)

    def test_update_service(self):
        """Test updating a service."""
        self.service.update_service(self.session, type="Maintenance")
        service = Service.get_service_by_id(self.session, self.service.service_id)
        self.assertEqual(service.type, "Maintenance")

if __name__ == '__main__':
    unittest.main()
