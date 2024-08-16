#!/usr/bin/python3
""" storage file """
import json
import os


class FileStorage:
    """ storage file class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ get the dictionary """
        return (FileStorage.__objects)

    def new(self, obj):
        """ set obj """
        ke = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[ke] = obj

    def save(self):
        """ serialize """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """ deserializes """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            dic_obj = json.load(f)
            FileStorage.__objects = dic_obj
