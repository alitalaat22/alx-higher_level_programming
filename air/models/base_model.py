#!/usr/bin/python3
import uuid
from datetime import datetime
class BaseModel:
    def __init__(self, *args, **kwrgs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        print(f"date of created \n{self.created_at}")
        self.update_at = datetime.now()
        print(f"date of update \n{self.update_at}")

    def save(self):
        self.update_at = datetime.now()

    
    def to_dict(self):
        cop = self.__dict__.copy()
        cop["__class__"] = type(self).__name__
        cop["created"] = datetime.isoformat(self.created_at)
        cop["update"] = self.update_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return cop

    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
