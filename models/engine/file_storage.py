#!/usr/bin/pytho3
""" file storage class """


class FileStorage:
    """
    the class
    """

    def __init__(self):
        """initializing the class """
        self.__objects = {}

    def all(self):
        """ return the dictionary """
        return self.__objects

    def new(self, obj):
        """ add a new object to the dictionary """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ serialize the dictionary """
    obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
    with open(self.__file_path, 'w') as f:
        json.dump(obj_dict, f)

    def reload(self):
        """ deserialize the dictionary """
         if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    cls = eval(class_name)
                    self.__objects[key] = cls(**value)
