#!/usr/bin/python3
"""this"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """this """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.height = value
        self.width = value

    def update(self, *args, **kwargs):
        """this"""
        attrs = ['id', 'size', 'x', 'y']
        for index, value in zip(attrs, args):
            setattr(self, index, value)
        for key, value in kwargs.items():
            setattr(self, key, value)
