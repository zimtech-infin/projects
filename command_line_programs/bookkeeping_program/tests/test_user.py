# tests/test_user.py

import unittest
from models.user import User, Session

class TestUser(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures."""
        self.session = Session()
        self.user = User(name="John Doe", role="Admin", contact_info="john@example.com")
        self.user.add_user(self.session)

    def tearDown(self):
        """Clean up test fixtures."""
        self.session.query(User).delete()
        self.session.commit()
        self.session.close()

    def test_add_user(self):
        """Test adding a user."""
        user = User.get_user_by_id(self.session, self.user.user_id)
        self.assertIsNotNone(user)
        self.assertEqual(user.name, "John Doe")

    def test_remove_user(self):
        """Test removing a user."""
        self.user.remove_user(self.session)
        user = User.get_user_by_id(self.session, self.user.user_id)
        self.assertIsNone(user)

    def test_update_user(self):
        """Test updating a user."""
        self.user.update_user(self.session, name="Jane Doe")
        user = User.get_user_by_id(self.session, self.user.user_id)
        self.assertEqual(user.name, "Jane Doe")

if __name__ == '__main__':
    unittest.main()
