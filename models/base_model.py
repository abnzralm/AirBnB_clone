#!/usr/bin/python3
"""This module contains the class BaseModel"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
        The BaseModel class that defines all common attributes
        and methods.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the instance.

        Attributes:
            created_at (datetime): Current datetime.
            updated_at (datetime): updated whenever the obj is changed.
            id (str): Unique identifier assigned.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "updated_at" or key == "created_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            models.strge.new(self)

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with
            the current datetime"""

        self.updated_at = datetime.now()
        # models.strge.new(self)
        models.strge.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""

        diCpy = self.__dict__.copy()
        diCpy["__class__"] = self.__class__.__name__
        diCpy["created_at"] = self.created_at.isoformat()
        diCpy["updated_at"] = self.updated_at.isoformat()
        return diCpy
