#!/usr/bin/python3
"""
Defines a class "City" which inherits from BaseModel class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class "City" which inherits from 
    BaseModel and has public attributes
    """
    name = ""
    state_id = ""
