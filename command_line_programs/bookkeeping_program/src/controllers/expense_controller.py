# src/controllers/expense_controller.py

from models.expense import Expense, Session

class ExpenseController:
    """Controller to manage expense-related operations."""

    def __init__(self):
        self.session = Session()

    def log_expense(self, category, amount, date, description):
        """Log a new expense."""
        expense = Expense(category=category, amount=amount, date=date, description=description)
        expense.log_expense(self.session)
        return expense

    def delete_expense(self, expense_id):
        """Delete an expense."""
        expense = Expense.get_expense_by_id(self.session, expense_id)
        if expense:
            expense.delete_expense(self.session)
            return True
        return False

    def update_expense(self, expense_id, category=None, amount=None, date=None, description=None):
        """Update an existing expense."""
        expense = Expense.get_expense_by_id(self.session, expense_id)
        if expense:
            expense.update_expense(self.session, category=category, amount=amount, date=date, description=description)
            return True
        return False

    def get_expense_by_id(self, expense_id):
        """Retrieve an expense by its ID."""
        return Expense.get_expense_by_id(self.session, expense_id)
