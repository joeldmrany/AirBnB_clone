#!/usr/bin/python3
"""
base model class
"""
import uuid
from datetime import datetime
import models

class BaseModel():
    """ Base Model calss """

    def __init__(self, *args, **kwargs):
        """ Initializing of a new BaseModel """
        time_form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_form)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """ save the model """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """ returns dictionary for base model """
        cp_dict = self.__dict__.copy()
        cp_dict["created_at"] = self.created_at.isoformat()
        cp_dict["updated_at"] = self.updated_at.isoformat()
        cp_dict["__class__"] = self.__class__.__name__
        return cp_dict

    def __str__(self):
        """ representation of the model """
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)
