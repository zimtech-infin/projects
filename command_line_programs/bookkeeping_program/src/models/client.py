# src/models/client.py

import sys
import os
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

# Adjust the path to ensure imports work correctly when running the file directly
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, '..'))

# Importing Base and engine from user.py for shared database setup
from models.user import Base, engine

# Client model definition using SQLAlchemy ORM
class Client(Base):
    """Represents a client for home services."""
    
    __tablename__ = 'clients'

    client_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    contact_info = Column(String, nullable=False)
    service_history = Column(String)  # This field can be used to store a serialized list of service history

    def __init__(self, name, contact_info, service_history=None):
        """Initialize a new client instance."""
        self.name = name
        self.contact_info = contact_info
        self.service_history = service_history or ""

    def add_client(self, session):
        """Add a new client to the system."""
        session.add(self)
        session.commit()

    def remove_client(self, session):
        """Remove a client from the system."""
        session.delete(self)
        session.commit()

    def update_client(self, session, name=None, contact_info=None, service_history=None):
        """Update client information in the system."""
        if name:
            self.name = name
        if contact_info:
            self.contact_info = contact_info
        if service_history:
            self.service_history = service_history
        session.commit()

    @staticmethod
    def get_client_by_id(session, client_id):
        """Retrieve a client by their ID."""
        return session.query(Client).filter(Client.client_id == client_id).first()

# Ensure the models are created in the database
Base.metadata.create_all(engine)

# Session setup
Session = sessionmaker(bind=engine)
