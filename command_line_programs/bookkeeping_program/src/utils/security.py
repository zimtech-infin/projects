# src/utils/security.py

import hashlib
import os

class Security:
    """Utility class for managing security measures."""

    @staticmethod
    def hash_password(password):
        """Hash a password for secure storage."""
        salt = os.urandom(32)  # Generate a random salt
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return salt + hashed_password  # Store salt with hashed password

    @staticmethod
    def verify_password(stored_password, provided_password):
        """Verify a stored password against one provided by user."""
        salt = stored_password[:32]  # Extract the salt
        stored_hash = stored_password[32:]
        provided_hash = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt, 100000)
        return stored_hash == provided_hash
