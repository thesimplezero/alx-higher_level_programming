#!/usr/bin/python3
"""Module to find the max integer in a list"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers.
    If the list is empty, the function returns None.

    Args:
        list (list): The list of integers.

    Returns:
        int: The maximum integer in the list, or None if the list is empty.
    """
    return max(list) if list else None
