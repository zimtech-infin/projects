# src/utils/data_backup.py

import shutil
import os

class DataBackup:
    """Utility class for data backup operations."""

    @staticmethod
    def backup_data(db_path, backup_path):
        """Backup system data to a specified location."""
        try:
            shutil.copy(db_path, backup_path)
            print(f"Data backup successful to {backup_path}.")
        except Exception as e:
            print(f"Data backup failed: {e}")
