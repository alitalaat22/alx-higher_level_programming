#!/usr/bin/python3


class Square:

        def __init__(self, size=0):
                self.__size = size

        def area(self):
                return self.__size * self.__size

        @property
        def size(self):
                """Property for attribute size"""
                return self.__size

        @size.setter
        def size(self, value):
                """Setter for attribute size"""
                if type(value) != int:
                        print("size must be an integer", end="")
                        raise TypeError
                elif value < 0:
                        print("size must be >= 0", end="")
                        raise ValueError
                else:
                        self.__size = value