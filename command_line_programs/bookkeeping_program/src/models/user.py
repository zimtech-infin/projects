# src/models/user.py

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base class for declarative class definitions.
Base = declarative_base()

class User(Base):
    """Represents a user in the system."""

    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    contact_info = Column(String, nullable=False)

    def __init__(self, name, role, contact_info):
        self.name = name
        self.role = role
        self.contact_info = contact_info

    def add_user(self, session):
        """Add a new user to the system."""
        session.add(self)
        session.commit()

    def remove_user(self, session):
        """Remove an existing user from the system."""
        session.delete(self)
        session.commit()

    def update_user(self, session, name=None, role=None, contact_info=None):
        """Update user information in the system."""
        if name:
            self.name = name
        if role:
            self.role = role
        if contact_info:
            self.contact_info = contact_info
        session.commit()

    @staticmethod
    def get_user_by_id(session, user_id):
        """Retrieve a user by their ID."""
        return session.query(User).filter(User.user_id == user_id).first()

# Database setup
engine = create_engine('sqlite:///home_services.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
