#!/usr/bin/python3

"""
This module contains the function 'save_to_json_file' which writes an object
to a text file, using a JSON representation.

The function employs the 'json' module to convert the object into a JSON
representation and writes this to a specified file. It does not handle
exceptions in cases where the object can't be serialized or file permissions
are insufficient.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON representation.

    Args:
        my_obj: The object to be written to the file.
        filename (str): The name of the file to write the object to.

    Returns:
        None
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
