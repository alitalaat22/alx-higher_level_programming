#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods for other classes"""
import uuid
from datetime import datetime
class BaseModel:
    """Class from which all other classes will inherit"""
    def __init__(self, *args, **kwrgs):
        """Initializes instance attributes

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        print(f"date of created \n{self.created_at}")
        self.update_at = datetime.now()
        print(f"date of update \n{self.update_at}")

    def save(self):
        """updates the public instance attribute updated_at"""
        self.update_at = datetime.now()

    
    def to_dict(self):
        """
        returns a new copy of dictionary
        added '__class__' key
        Updated time to isoformat
        """
        cop = self.__dict__.copy()
        cop["__class__"] = type(self).__name__
        cop["created"] = datetime.isoformat(self.created_at)
        cop["update"] = self.update_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return cop

    def __str__(self):
        """Prints Classname, instance id, and dictionary"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
