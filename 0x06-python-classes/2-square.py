#!/usr/bin/python3


class Square:
        """Creating a class called Square"""
        def __init__(self, size=0):
                """Creating special method init with attribute size"""
                if type(size) != int:
                        print("size must be an integer", end="")
                        raise TypeError
                elif size < 0:
                        print("size must be >= 0", end="")
                        raise ValueError
                else:
                        self.__size = size