#!/usr/bin/python3
"""
Module to add two numbers.
This module provides a function to add two numbers which can be either of type
integer or float. In case of float, they are cast to integer before addition.
"""


def add_integer(a, b=98):
    """
    Return the addition of a and b as integers.
    Floats are typecast to integers before addition.

    Args:
        a (int or float): The first number to add.
        b (int or float, optional): The second number to add. Defaults to 98.

    Raises:
        TypeError: If either a or b is not an integer or a float.

    Returns:
        int: The result of the addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
