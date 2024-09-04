#!/usr/bin/python3
"""
This module defines the Square class, which is a special case of a rectangle.
It inherits from the Rectangle class and represents squares, which have equal
width and height.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square, which is a specific
    type of rectangle with equal sides.
    Inherits from the Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square's sides.
            x (int): The x-coordinate of the square.
            y (int): The y-coordinate of the square.
            id (int): The id of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the Square instance.

        Returns:
            str: String representation of the Square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square's sides.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square, updating both width and height.

        Args:
            value (int): The new size of the square's sides.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.height = value
        self.width = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Square.

        Args:
            *args: Non-keyword arguments in the order of id, size, x, y.
            **kwargs: Keyword arguments to update attributes by name.
        """
        attrs = ['id', 'size', 'x', 'y']
        for index, value in zip(attrs, args):
            setattr(self, index, value)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the Rectangle instance"""
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}
