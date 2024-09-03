# src/models/service.py

import sys
import os
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker

# Adjust the path to ensure imports work correctly when running the file directly
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, '..'))

# Importing Base and engine from user.py for shared database setup
from models.user import Base, engine

class Service(Base):
    """Represents a service provided to a client."""

    __tablename__ = 'services'

    service_id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    client_id = Column(Integer, nullable=False)

    def __init__(self, type, date, client_id):
        """Initialize a new service instance."""
        self.type = type
        self.date = date
        self.client_id = client_id

    def add_service(self, session):
        """Add a new service to the client's service history."""
        session.add(self)
        session.commit()

    def remove_service(self, session):
        """Remove a service from the client's service history."""
        session.delete(self)
        session.commit()

    def update_service(self, session, type=None, date=None, client_id=None):
        """Update service details in the system."""
        if type:
            self.type = type
        if date:
            self.date = date
        if client_id:
            self.client_id = client_id
        session.commit()

    @staticmethod
    def get_service_by_id(session, service_id):
        """Retrieve a service by its ID."""
        return session.query(Service).filter(Service.service_id == service_id).first()

# Ensure the models are created in the database
Base.metadata.create_all(engine)

# Session setup
Session = sessionmaker(bind=engine)
