#!/usr/bin/python3
"""
Module that defines the base class from 
which all other classes inherit
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    BaseModel class that acts as the 
    superclass for all other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Class constructor
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                else:
                    setattr(self, key, datetime.fromisoformat(value) if key == "created_at" or key == "updated_at" else value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """String representation of an instance"""
        return (
            "[{}] [{}] {}".format(self.__class__.__name__,
                                  self.id, self.__dict__))
    def save(self):
        """Updates the public instance attribute updated_at"""
        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns that dictionary representation of an instance"""
        dict_q = {key: value for key, value in self.__dict__.items()}
        class_name = {'__class__': self.__class__.__name__}
        dict_q.update(class_name)

        for key, value in dict_q.items():
            if key == 'created_at':
                dict_q[key] = self.created_at.isoformat(sep='T')
            elif key == 'updated_at':
                dict_q[key] = self.updated_at.isoformat(sep='T')

        return (dict_q)

