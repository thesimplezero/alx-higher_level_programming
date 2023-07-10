#!/usr/bin/python3
"""
This module contains a function that checks if an object is an instance of a
class that it inherited from (directly or indirectly).
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that it inherited from
    (directly or indirectly).

    Parameters:
    obj (any): The object to check.
    a_class (type): The class to match the type of obj to.

    Returns:
    True if obj is an instance of a class that it inherited from
    (directly or indirectly). Otherwise, it returns False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
