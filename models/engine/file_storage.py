#!/usr/bin/python3
""" storage file """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ storage file class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ get the dictionary """
        return FileStorage.__objects

    def new(self, obj):
        """ set obj """
        ke = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ke, obj.id)] = obj

    def save(self):
        """ serialize """
        o_dict = FileStorage.__objects
        obj_dict = {obj: o_dict[obj].to_dict() for obj in o_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """ deserializes """
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for o in obj_dict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
