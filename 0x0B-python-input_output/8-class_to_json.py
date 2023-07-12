#!/usr/bin/python3
"""
This module defines a function 'class_to_json' that returns a dictionary
representation of a simple data structure for JSON serialization.

The function takes an object instance of a class as an argument. It assumes 
all attributes of the object are serializable: list, dictionary, string, 
integer, and boolean. No module is imported in this script.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON 
    serialization of an object.

    Parameters:
    obj (obj): Instance of a class.

    Returns:
    obj.__dict__: A dictionary representation of the object.
    """
    return obj.__dict__
