# tests/test_client.py

import unittest
from models.client import Client, Session

class TestClient(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures."""
        self.session = Session()
        self.client = Client(name="Jane Doe", contact_info="jane@example.com")
        self.client.add_client(self.session)

    def tearDown(self):
        """Clean up test fixtures."""
        self.session.query(Client).delete()
        self.session.commit()
        self.session.close()

    def test_add_client(self):
        """Test adding a client."""
        client = Client.get_client_by_id(self.session, self.client.client_id)
        self.assertIsNotNone(client)
        self.assertEqual(client.name, "Jane Doe")

    def test_remove_client(self):
        """Test removing a client."""
        self.client.remove_client(self.session)
        client = Client.get_client_by_id(self.session, self.client.client_id)
        self.assertIsNone(client)

    def test_update_client(self):
        """Test updating a client."""
        self.client.update_client(self.session, name="John Smith")
        client = Client.get_client_by_id(self.session, self.client.client_id)
        self.assertEqual(client.name, "John Smith")

if __name__ == '__main__':
    unittest.main()
