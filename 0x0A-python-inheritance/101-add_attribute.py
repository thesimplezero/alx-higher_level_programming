#!/usr/bin/python3
"""
This module provides a function 'add_attribute'
which attempts to add a new attribute to an object.
"""


def add_attribute(obj, att, value):
    """
    Attempts to add a new attribute to an object.

    Parameters:
        obj (any): The object to which an attribute should be added.
        att (str): The name of the attribute to add.
        value (any): The value to set the new attribute to.

    Raises:
        TypeError: If the attribute can't be added to the object.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
