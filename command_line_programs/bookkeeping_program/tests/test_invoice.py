# tests/test_invoice.py

import unittest
from models.invoice import Invoice, Session
from datetime import date

class TestInvoice(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.session = Session()
        # Create a sample invoice object for testing
        self.invoice = Invoice(service_id=1, amount=150.0, status="Pending", due_date=date(2024, 9, 15))
        self.invoice.create_invoice(self.session)

    def tearDown(self):
        """Clean up test fixtures after each test method."""
        self.session.query(Invoice).delete()  # Delete all entries in the Invoice table
        self.session.commit()
        self.session.close()

    def test_create_invoice(self):
        """Test creating an invoice."""
        invoice = Invoice.get_invoice_by_id(self.session, self.invoice.invoice_id)
        self.assertIsNotNone(invoice)
        self.assertEqual(invoice.amount, 150.0)
        self.assertEqual(invoice.status, "Pending")

    def test_delete_invoice(self):
        """Test deleting an invoice."""
        self.invoice.delete_invoice(self.session)
        invoice = Invoice.get_invoice_by_id(self.session, self.invoice.invoice_id)
        self.assertIsNone(invoice)

    def test_update_invoice(self):
        """Test updating an invoice."""
        self.invoice.update_invoice(self.session, amount=200.0, status="Paid")
        invoice = Invoice.get_invoice_by_id(self.session, self.invoice.invoice_id)
        self.assertEqual(invoice.amount, 200.0)
        self.assertEqual(invoice.status, "Paid")

if __name__ == '__main__':
    unittest.main()
