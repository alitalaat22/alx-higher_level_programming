#!/usr/bin/python3
"""This module defines a Rectangle class that inherits from Base."""

from base import Base


class Rectangle(Base):
    """Represents a rectangle shape, inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle. Default is 0.
            y (int): The y-coordinate of the rectangle. Default is 0.
            id (int, optional): The ID of the rectangle. If not provided,
            it will be automatically assigned by the Base class.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            ValueError: If the value is not a positive integer.
        """
        if type(value) is not int or value <= 0:
            raise ValueError("width must be an integer > 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            ValueError: If the value is not a positive integer.
        """
        if type(value) is not int or value <= 0:
            raise ValueError("height must be an integer > 0")
        self.__height = value

    @property
    def x(self):
        """
        Get the x-coordinate of the rectangle.

        Returns:
            int: The x-coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x-coordinate of the rectangle.

        Args:
            value (int): The new x-coordinate value.

        Raises:
            ValueError: If the value is not a non-negative integer.
        """
        if type(value) is not int or value < 0:
            raise ValueError("x must be an integer >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Get the y-coordinate of the rectangle.

        Returns:
            int: The y-coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y-coordinate of the rectangle.

        Args:
            value (int): The new y-coordinate value.

        Raises:
            ValueError: If the value is not a non-negative integer.
        """
        self.__y = value
