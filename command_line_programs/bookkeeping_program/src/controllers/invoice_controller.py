# src/controllers/invoice_controller.py

from models.invoice import Invoice, Session

class InvoiceController:
    """Controller to manage invoice-related operations."""

    def __init__(self):
        self.session = Session()

    def create_invoice(self, service_id, amount, status, due_date):
        """Create a new invoice."""
        invoice = Invoice(service_id=service_id, amount=amount, status=status, due_date=due_date)
        invoice.create_invoice(self.session)
        return invoice

    def delete_invoice(self, invoice_id):
        """Delete an invoice."""
        invoice = Invoice.get_invoice_by_id(self.session, invoice_id)
        if invoice:
            invoice.delete_invoice(self.session)
            return True
        return False

    def update_invoice(self, invoice_id, amount=None, status=None, due_date=None):
        """Update an existing invoice."""
        invoice = Invoice.get_invoice_by_id(self.session, invoice_id)
        if invoice:
            invoice.update_invoice(self.session, amount=amount, status=status, due_date=due_date)
            return True
        return False

    def get_invoice_by_id(self, invoice_id):
        """Retrieve an invoice by its ID."""
        return Invoice.get_invoice_by_id(self.session, invoice_id)
