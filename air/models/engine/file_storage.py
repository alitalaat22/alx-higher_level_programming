#!/usr/bin/python3
"""Module مسؤول عن التخزين والبيانات"""
import datetime
import os
import json

class FileStorage:
    """storage for data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dict of __object"""
        return FileStorage.__objects

    def new(self, obj):
        """Assigns the object with key '<object class name>.id' in the '__objects' dictionary"""
        key = f"{type(obj).__name__}.{obj.id}"
        """type(obj).__name__, obj.id"""
        FileStorage.__objects[key] = obj

    def save(self):
        """Converts '__objects' into a JSON format and saves it to the file specified by '__file_path'"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as pato:
            damo = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
            json.dump(damo, pato)

    def classes(self):
        """dict valid classes and references"""
        from models.base_model import BaseModel
        from models.state import State
        from models.review import Review
        from models.city import City
        from models.amenity import Amenity
        from models.user import User
        from models.place import Place

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """Reload  stored"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as pato:
            obj_dict = json.load(pato)
            obj_dict = {key: self.classes()[v["__class__"]](**value)
                        for key, value in obj_dict.items()}
            # TODO: should this overwrite or insert?
            FileStorage.__objects = obj_dict

    def attributes(self):
        """Returns attributes and their types for class name"""
        attributes = {
            "BaseModel":
                     {"id": str,
                      "created_at": datetime.datetime,
                      "updated_at": datetime.datetime},
            "User":
                     {"email": str,
                      "password": str,
                      "first_name": str,
                      "last_name": str},
            "State":
                     {"name": str},
            "City":
                     {"state_id": str,
                      "name": str},
            "Amenity":
                     {"name": str},
            "Place":
                     {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review":
            {"place_id": str,
                         "user_id": str,
                         "text": str}
        }
        return attributes
