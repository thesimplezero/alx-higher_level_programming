#!/usr/bin/python3

"""
This module contains the function 'append_write', which appends a string
to the end of a UTF8 text file and returns the number of characters added.

The function provides a simple means to append text to files, with automatic
file creation if it doesn't already exist.
"""


def append_write(filename="", text=""):
    """
    Appends a string to a UTF8 text file and returns the
    number of characters added.

    Args:
        filename (str): The name of the file to append to.
        Defaults to an empty string.
        text (str): The text to append to the file.
        Defaults to an empty string.

    Returns:
        int: Number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
