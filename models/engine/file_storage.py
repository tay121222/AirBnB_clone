#!/usr/bin/python3
"""FIlestorage class"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        obj_dict = {
                key: obj.to_dict() for key,
                obj in FileStorage.__objects.items()
                }
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if not os.path.exists(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
            obj_dict = json.load(f)
            for key, value in obj_dict.items():
                class_name, obj_id = key.split('.')
                class_ref = eval(class_name)
                FileStorage.__objects[key] = class_ref(**value)

    def classes(self):
        return {
                'BaseModel': BaseModel,
                'User': User,
                'State': State,
                'City': City,
                'Place:' Place,
                'Amenity': Amenity,
                'Review': Review
                }
