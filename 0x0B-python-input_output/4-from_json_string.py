#!/usr/bin/python3

"""
This module contains the function 'from_json_string' which converts a JSON
string into a Python object (data structure).

The function employs the 'json' module to transform a JSON string into a Python
data structure. It does not handle exceptions in cases where the
JSON string does not represent a valid object.
"""

import json


def from_json_string(my_str):
    """
    Returns the Python data structure represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert into a Python object.

    Returns:
        The Python data structure represented by 'my_str'.
    """
    return json.loads(my_str)
