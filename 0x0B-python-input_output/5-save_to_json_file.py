#!/usr/bin/python3
"""
This module contains a function that saves
a Python object to a file in JSON format.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function writes a Python object to
    text file using its JSON representation.

    Args:
        my_obj (object): The Python object to be saved.
        filename (str): The name of the file where the object will be saved.

    The file is opened in write mode, and the object
    is converted to JSON format before being saved.
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
