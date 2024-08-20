#!/usr/bin/python3
"""
write function convert str to json file
"""
import json


def to_json_string(my_obj):
    """
    This function returns the JSON representation of an object.
    arg: my_obj is a Python object (e.g., dict, list, str, etc.)
    The variable json_string stores the JSON formatted string.
    Returns json_string after converting the object to JSON format.
    """
    json_string = json.dumps(my_obj)
    return json_string
