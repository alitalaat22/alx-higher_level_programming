#!/usr/bin/python3


class Square:
        """Creating a class called Square"""
        def __init__(self, size=0):
                """Creating a special method for Square"""
                self.__size = size

        def area(self):
                """Creating a public instance method called area"""
                return self.__size * self.__size

        def my_print(self):
                """Creating a public instance method called my_print"""
                if self.size == 0:
                        print()
                for i in range(self.__size):
                        print("{}".format("#" * self.__size))

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