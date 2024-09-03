# src/models/expense.py

import sys
import os
from sqlalchemy import Column, Integer, Float, String, Date
from sqlalchemy.orm import sessionmaker

# Adjust the path to ensure imports work correctly when running the file directly
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, '..'))

# Importing Base and engine from user.py for shared database setup
from models.user import Base, engine

class Expense(Base):
    """Represents a business expense."""

    __tablename__ = 'expenses'

    expense_id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    description = Column(String)

    def __init__(self, category, amount, date, description):
        """Initialize a new expense instance."""
        self.category = category
        self.amount = amount
        self.date = date
        self.description = description

    def log_expense(self, session):
        """Log a new expense."""
        session.add(self)
        session.commit()

    def update_expense(self, session, category=None, amount=None, date=None, description=None):
        """Update expense details in the system."""
        if category:
            self.category = category
        if amount:
            self.amount = amount
        if date:
            self.date = date
        if description:
            self.description = description
        session.commit()

    def delete_expense(self, session):
        """Delete an expense from the system."""
        session.delete(self)
        session.commit()

    @staticmethod
    def get_expense_by_id(session, expense_id):
        """Retrieve an expense by its ID."""
        return session.query(Expense).filter(Expense.expense_id == expense_id).first()

# Ensure the models are created in the database
Base.metadata.create_all(engine)

# Session setup
Session = sessionmaker(bind=engine)
