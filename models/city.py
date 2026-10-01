#!/usr/bin/python3
"""
City Module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class inheriting from BaseModel
    """
    state_id = ""
    name = ""
