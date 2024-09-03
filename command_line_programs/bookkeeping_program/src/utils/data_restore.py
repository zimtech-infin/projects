# src/utils/data_restore.py

import shutil
import os

class DataRestore:
    """Utility class for data restoration operations."""

    @staticmethod
    def restore_data(backup_path, db_path):
        """Restore system data from a backup."""
        try:
            shutil.copy(backup_path, db_path)
            print(f"Data restored successfully from {backup_path}.")
        except Exception as e:
            print(f"Data restore failed: {e}")
