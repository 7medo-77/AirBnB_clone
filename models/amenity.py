#!/usr/bin/python3
"""
Defines a class "Amenity" which inherits from BaseModel class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Class "Amenity" which inherits from 
    BaseModel and has public attributes
    """
    name = ""
