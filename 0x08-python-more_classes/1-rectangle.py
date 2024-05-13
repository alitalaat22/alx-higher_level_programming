#!/usr/bin/python3
#by ali elshaer
"""A class that defines a rectangle"""

class Rectangle:
    """that defines a rectangle """
    def __init__ (self, width=0, height=0):
        """Initializing this rectangle class
        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """        
        self.__width = width
        self.__height = height
    @property
    def width(self):
        """property width to retrieve it"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """property setter width to set it"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
        """property height to retrieve it"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """property setter height to set it"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0 :
            raise ValueError("height must be >= 0")
        self.__height = value
