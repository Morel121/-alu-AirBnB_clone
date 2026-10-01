#!/usr/bin/python3
"""
User Module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class inheriting from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
