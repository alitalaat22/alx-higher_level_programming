#!/usr/bin/python3
"""This class will be the “base” of all other classes in this project"""


import json
import os


class Base:
    """this a main class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """this method assig id for  nb obj"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """thisfjjf;l
        asjdfklja;ldkfkajfla"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """thsofjklasjf
        f;ladsfjlkjaf;lk;"""
        with open(cls.__name__ + ".json", "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                s = []
                for obj in list_objs:
                    s.append(obj.to_dictionary())

                f.write(cls.to_json_string(s))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with all attributes already set"""
        dummy_instance = cls(1, 1)  # Use default values
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Load list of instances from JSON file"""
        filename = cls.__name__ + ".json"
        if not os.path.isfile(filename):
            return []

        with open(filename, "r") as f:
            json_string = f.read()

        dictionaries = cls.from_json_string(json_string)
        instances = [cls.create(**d) for d in dictionaries]

        return instances
