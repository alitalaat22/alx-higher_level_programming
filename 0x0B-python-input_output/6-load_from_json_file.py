#!/usr/bin/python3
""" this module contanis a function that creats an object from a json file """
import json


def load_from_json_file(filename):
    """
    This function reads a JSON file
    returns the corresponding Python object
    Args:
    filename (STR): the name of the file to be read

    Returns:
    object: The python object represented by the JSON contant of the file
    """
    with open(filename, "r") as jslo:
        json.load(jslo)
