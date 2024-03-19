#!/usr/bin/python3
"""
Defines a class user which inherits from BaseModel class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class User which inherits from BaseModel and has public attributes
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
