#!/usr/bin/python3

"""
This module contains the function 'load_from_json_file' which creates a Python
object from a given JSON file.

The function uses the 'json' module to parse a JSON string stored
in a file into a Python data type. The function does not
manage exceptions for cases where the JSON string does
not represent an object, or when file permissions are insufficient.
"""

import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Args:
        filename (str): The name of the file from which to load the object.

    Returns:
        Python data type object parsed from the JSON string in the file.
    """
    with open(filename) as f:
        return json.load(f)
