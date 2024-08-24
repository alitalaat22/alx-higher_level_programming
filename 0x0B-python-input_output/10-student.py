#!/usr/bin/python3
"""This module defines a Student class."""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        tjos o
        sdfk
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """this func is comid'"""
        if attrs is None:
            return self.__dict__
        else:
            s = {}
            for attr in attrs:
                if attr in self.__dict__:

                    s[attr] = self.__dict__[attr]
            return s
