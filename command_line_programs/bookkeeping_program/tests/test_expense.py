# tests/test_expense.py

import unittest
from models.expense import Expense, Session
from datetime import date

class TestExpense(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.session = Session()
        # Create a sample expense object for testing
        self.expense = Expense(category="Office Supplies", amount=50.0, date=date(2024, 9, 1), description="Stationery")
        self.expense.log_expense(self.session)

    def tearDown(self):
        """Clean up test fixtures after each test method."""
        self.session.query(Expense).delete()  # Delete all entries in the Expense table
        self.session.commit()
        self.session.close()

    def test_log_expense(self):
        """Test logging an expense."""
        expense = Expense.get_expense_by_id(self.session, self.expense.expense_id)
        self.assertIsNotNone(expense)
        self.assertEqual(expense.category, "Office Supplies")
        self.assertEqual(expense.amount, 50.0)

    def test_delete_expense(self):
        """Test deleting an expense."""
        self.expense.delete_expense(self.session)
        expense = Expense.get_expense_by_id(self.session, self.expense.expense_id)
        self.assertIsNone(expense)

    def test_update_expense(self):
        """Test updating an expense."""
        self.expense.update_expense(self.session, category="IT Equipment", amount=100.0)
        expense = Expense.get_expense_by_id(self.session, self.expense.expense_id)
        self.assertEqual(expense.category, "IT Equipment")
        self.assertEqual(expense.amount, 100.0)

if __name__ == '__main__':
    unittest.main()
