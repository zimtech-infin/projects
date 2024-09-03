# src/views/expense_view.py

import sys
import os

# Adjust the path to ensure imports work correctly when running the file directly
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, '..'))

# Importing the ExpenseController from the controllers module
from controllers.expense_controller import ExpenseController

class ExpenseView:
    """View to interact with expense operations in the system."""

    def __init__(self):
        self.expense_controller = ExpenseController()

    def display_expense_info(self, expense_id):
        """Display expense information by ID."""
        expense = self.expense_controller.get_expense_by_id(expense_id)
        if expense:
            print(f"Expense ID: {expense.expense_id}, Category: {expense.category}, Amount: {expense.amount}, Date: {expense.date}, Description: {expense.description}")
        else:
            print(f"No expense found with ID: {expense_id}")

    def log_expense_form(self):
        """Simulate a form to log a new expense."""
        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: "))
        date = input("Enter expense date (YYYY-MM-DD): ")
        description = input("Enter expense description: ")
        self.expense_controller.log_expense(category=category, amount=amount, date=date, description=description)
        print("Expense logged successfully.")

    def delete_expense_form(self):
        """Simulate a form to delete an expense."""
        expense_id = int(input("Enter expense ID to delete: "))
        if self.expense_controller.delete_expense(expense_id):
            print("Expense deleted successfully.")
        else:
            print("Expense not found.")

    def update_expense_form(self):
        """Simulate a form to update an expense."""
        expense_id = int(input("Enter expense ID to update: "))
        category = input("Enter new expense category (leave blank to keep current): ")
        amount = input("Enter new expense amount (leave blank to keep current): ")
        date = input("Enter new expense date (leave blank to keep current, format: YYYY-MM-DD): ")
        description = input("Enter new expense description (leave blank to keep current): ")
        self.expense_controller.update_expense(expense_id, category=category, amount=amount, date=date, description=description)
        print("Expense updated successfully.")

# Entry point for the script
if __name__ == "__main__":
    expense_view = ExpenseView()
    expense_view.log_expense_form()  # Example action
