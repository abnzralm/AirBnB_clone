#!/usr/bin/python3
"""This module contains the Filetorage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
        Serializes instances to a JSON file and
        deserializes JSON file to instances.

        Attributes:
            __fp (str): Path to the JSON file.
            __ob (dict): Stores all objects.
    """

    __fp = "file.json"
    __ob = {}

    def all(self):
        """ returns the dictionary __ob """

        return FileStorage.__ob

    def new(self, obj):
        """sets in __ob the obj with key <obj class name>.id"""

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__ob[key] = obj

    def save(self):
        """ serializes __ob to the JSON file """
        path = FileStorage.__fp

        new_oj = {k: FileStorage.__ob[k].to_dict(
        ) for k in FileStorage.__ob.keys()}

        with open(path, "w") as file:
            json.dump(new_oj, file)

    def reload(self):
        """Deserialize the JSON file __fp to __ob, if it exists."""

        path = FileStorage.__fp

        try:
            with open(path) as file:
                objson = json.load(file)
                for obj in objson.values():
                    cls_nme = obj['__class__']
                    del obj['__class__']
                    self.new(eval(cls_nme)(**obj))

        except FileNotFoundError:
            return
