#!/usr/bin/python3
"""
Initialize models package and set up storage instance.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
