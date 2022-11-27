#!/usr/bin/python3
"""
creating a unique filestorage instance for
application
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
