#!/usr/bin/python3
"""
This function appends a string at the end of a text file (UTF-8)
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF-8) and returns
    the number of characters added.
    
    Args:
        filename (str): The name of the file to append the text to.
        text (str): The string to append to the file.
    
    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
