#!/usr/bin/python3
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file
    to instances.

    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary to store serialized objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.

        Returns:
            dict: The dictionary of serialized objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets the given object in __objects with the key <obj class name>.id.

        Args:
            obj: An instance of a class.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (__file_path).
        """
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes the JSON file (__file_path) to __objects.

        If the file doesn't exist, no exception should be raised.
        """
        try:
            with open(self.__file_path, "r") as file:
                serialized_objects = json.load(file)
                for key, value in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    if class_name == "BaseModel":
                        obj = BaseModel(**value)
                    elif class_name == "User":
                        obj = User(**value)
                    elif class_name == "State":
                        obj = State(**value)
                    elif class_name == "City":
                        obj = City(**value)
                    elif class_name == "Amenity":
                        obj = Amenity(**value)
                    elif class_name == "Place":
                        obj = Place(**value)
                    elif class_name == "Review":
                        obj = Review(**value)
                    else:
                        continue
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass