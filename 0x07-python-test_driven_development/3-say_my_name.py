#!/usr/bin/python3
"""Module to print full name."""


def say_my_name(first_name, last_name=""):
    """Print a formatted name.

    This function takes two parameters: first_name and last_name. It prints
    these parameters in the format: "My name is {first_name} {last_name}".

    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print, defaults to an empty string.

    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
