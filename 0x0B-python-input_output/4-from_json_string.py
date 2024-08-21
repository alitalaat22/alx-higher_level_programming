#!/usr/bin/python3
import json


def from_json_string(my_str):
    """
    This function takes a JSON string and returns the corresponding
    Python object.

    Args:
    - my_str (str): The JSON string to be converted.

    Returns:
    - The Python object represented by the JSON string.
    """
    return json.loads(my_str)
