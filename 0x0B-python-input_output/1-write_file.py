#!/usr/bin/python3

"""
This module contains a function, 'write_file', that writes a string to a
UTF8 text file and returns the number of characters written.

The function serves to simplify the process of writing strings to files,
with automatic file creation if it doesn't exist, and overwriting if it does.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a UTF8 text file, creates the file if it doesn't exist,
    overwrites if it does, and returns the number of characters written.

    Args:
        filename (str): Name of the file to write to.
        Defaults to an empty string.
        text (str): Text to write to the file. Defaults to an empty string.

    Returns:
        int: Number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
