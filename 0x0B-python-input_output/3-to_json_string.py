#!/usr/bin/python3

"""
This module contains the function 'to_json_string', which returns the JSON
representation of an input object.

The function employs the 'json' module to transform Python objects into
their JSON string representation. It does not handle serialization exceptions.
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an input object.

    Args:
        my_obj: The object to represent as a JSON string.

    Returns:
        str: The JSON string representation of 'my_obj'.
    """
    return json.dumps(my_obj)
