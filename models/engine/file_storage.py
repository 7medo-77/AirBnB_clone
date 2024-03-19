#!/usr/bin/python3 bash
"""
Module that defines a class which contains methods 
that save a JSON representation of a class
"""
import json
import os


class FileStorage:
    """
    FileStorage class that stores a json representation 
    of an instance of a class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return (FileStorage.__objects)
    
    def new(self, obj):
        """Appends a key of object_name + id to the dictionary"""
        key = obj.__class__.__name__ + "." + obj.id
        temp_dict = {key : obj}
        FileStorage.__objects.update(temp_dict)

    def save(self):
        """Serialization of object to JSON file"""
        serialized_objs = {}
        for key, obj in self.__objects.items():
            serialized_objs[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objs, file, indent=4)

    def reload(self):
        from models.base_model import BaseModel
        from models.user import User
        # from models.state import State
        # from models.city import City
        # from models.amenity import Amenity
        # from models.place import Place
        # from models.review import Review
        """Deserialization of JSON file to __objects attribute"""
        if not os.path.exists(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as file:
            obj_dict = json.load(file)
            classes = {
                "BaseModel": BaseModel,
                "User": User,
            }
            obj_dict = {
                key: classes[value["__class__"]](**value)
                for key, value in obj_dict.items()
            }
            FileStorage.__objects = obj_dict
