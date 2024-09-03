# src/views/invoice_view.py

import sys
import os

# Adjust the path to ensure imports work correctly when running the file directly
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, '..'))

# Importing the InvoiceController from the controllers module
from controllers.invoice_controller import InvoiceController

class InvoiceView:
    """View to interact with invoice operations in the system."""

    def __init__(self):
        self.invoice_controller = InvoiceController()

    def display_invoice_info(self, invoice_id):
        """Display invoice information by ID."""
        invoice = self.invoice_controller.get_invoice_by_id(invoice_id)
        if invoice:
            print(f"Invoice ID: {invoice.invoice_id}, Service ID: {invoice.service_id}, Amount: {invoice.amount}, Status: {invoice.status}, Due Date: {invoice.due_date}")
        else:
            print(f"No invoice found with ID: {invoice_id}")

    def create_invoice_form(self):
        """Simulate a form to create a new invoice."""
        service_id = int(input("Enter service ID for the invoice: "))
        amount = float(input("Enter invoice amount: "))
        status = input("Enter invoice status (e.g., Pending, Paid): ")
        due_date = input("Enter invoice due date (YYYY-MM-DD): ")
        self.invoice_controller.create_invoice(service_id=service_id, amount=amount, status=status, due_date=due_date)
        print("Invoice created successfully.")

    def delete_invoice_form(self):
        """Simulate a form to delete an invoice."""
        invoice_id = int(input("Enter invoice ID to delete: "))
        if self.invoice_controller.delete_invoice(invoice_id):
            print("Invoice deleted successfully.")
        else:
            print("Invoice not found.")

    def update_invoice_form(self):
        """Simulate a form to update an invoice."""
        invoice_id = int(input("Enter invoice ID to update: "))
        amount = input("Enter new invoice amount (leave blank to keep current): ")
        status = input("Enter new invoice status (leave blank to keep current): ")
        due_date = input("Enter new invoice due date (leave blank to keep current, format: YYYY-MM-DD): ")
        self.invoice_controller.update_invoice(invoice_id, amount=amount, status=status, due_date=due_date)
        print("Invoice updated successfully.")

# Entry point for the script
if __name__ == "__main__":
    invoice_view = InvoiceView()
    invoice_view.create_invoice_form()  # Example action
