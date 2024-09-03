# src/models/invoice.py

import sys
import os
from sqlalchemy import Column, Integer, Float, String, Date
from sqlalchemy.orm import sessionmaker

# Adjust the path to ensure imports work correctly when running the file directly
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, '..'))

# Importing Base and engine from user.py for shared database setup
from models.user import Base, engine

class Invoice(Base):
    """Represents an invoice for a service provided to a client."""

    __tablename__ = 'invoices'

    invoice_id = Column(Integer, primary_key=True, autoincrement=True)
    service_id = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String, nullable=False)
    due_date = Column(Date, nullable=False)

    def __init__(self, service_id, amount, status, due_date):
        """Initialize a new invoice instance."""
        self.service_id = service_id
        self.amount = amount
        self.status = status
        self.due_date = due_date

    def create_invoice(self, session):
        """Generate a new invoice."""
        session.add(self)
        session.commit()

    def update_invoice(self, session, amount=None, status=None, due_date=None):
        """Update invoice details in the system."""
        if amount:
            self.amount = amount
        if status:
            self.status = status
        if due_date:
            self.due_date = due_date
        session.commit()

    def delete_invoice(self, session):
        """Delete an invoice from the system."""
        session.delete(self)
        session.commit()

    @staticmethod
    def get_invoice_by_id(session, invoice_id):
        """Retrieve an invoice by its ID."""
        return session.query(Invoice).filter(Invoice.invoice_id == invoice_id).first()

# Ensure the models are created in the database
Base.metadata.create_all(engine)

# Session setup
Session = sessionmaker(bind=engine)
