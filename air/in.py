#!/usr/bin/python3
'''
this module creats an empty class
'''


class BaseGeometry:

    def area(self):
        '''this is public method for handling Errors'''
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        '''this method raise the 2 exception
        1- for is not int
        2- is les than 0 or equal 0'''
        if type(value) is not  int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
"""----------------------------"""

class Rectangle(BaseGeometry):
    """the class Rectangle that inherits from BaseGeometry (7-base_geometry.py)."""
    def __init__(self, width, height):
        '''the method init '''
        self.integer_validator('width', width)
        # self.integer_validator('hieght', height)
        self.__width = width
        self.__height = height
        self.integer_validator('height', height)
    def area(self):
        """the method return sub 2 value"""
        return self.__width * self.__height
    
    def __str__(self):
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
"---------------------------------------10 Square---------------------------------------"
class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)
    def area(self):
        return self.__size * self.__size
    def __str__(self):
        '''Return a string representation of the square'''
        return f"[{self.__class__.__name__}] {self.__size}\{self.__size}"
