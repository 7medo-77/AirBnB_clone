#!/usr/bin/python3
"""
Defines a class "Review" which inherits from BaseModel class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class "Review" which inherits from BaseModel and has public attributes
    """
    place_id = ""
    user_id = ""
    text = ""
