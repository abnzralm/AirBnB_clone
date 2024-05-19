#!/usr/bin/python3
"""This module contains the class BaseModel"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """The BaseModel class that defines all common attributes
            and methods.
    """

    def __init__(self, *args, **kwargs):
        """
            Initializes the instance.

            Attributes:
                created_at (datetime): Current datetime when the instance is created.
                updated_at (datetime): Current datetime when the instance is created, updated whenever the object is changed.
                id (str): Unique identifier assigned when the instance is created.
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

        dict_copied = self.__dict__.copy()
        dict_copied["__class__"] = self.__class__.__name__
        dict_copied["created_at"] = self.created_at.isoformat()
        dict_copied["updated_at"] = self.updated_at.isoformat()
        return dict_copied
