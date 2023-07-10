#!/usr/bin/python3
"""
This module contains a function that checks if an object is
exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of a given class

    Parameters:
    obj (any): The object to check.
    a_class (type): The class to match the type of obj to

    Returns:
    True if obj is exactly an instance of a_class. Otherwise, it returns False.
    """
    return type(obj) == a_class
