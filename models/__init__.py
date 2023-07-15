#!/usr/bin/python3
from models.engine.file_storage import FileStorage
"""
This module initializes the unique FileStorage instance for the application.
"""

# Create a unique FileStorage instance for the application
storage = FileStorage()

# Load any existing serialized data into the storage instance
storage.reload()
