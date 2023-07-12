#!/usr/bin/python3

"""
This module contains a function read_file that reads and prints the content
of a given text file to the standard output.

The purpose of the module is to provide a simple way of reading and printing
file content, with automatic resource management to ensure that the file
gets closed after its content is printed. This function does not manage
file permissions or non-existing files exceptions.
"""


def read_file(filename=""):
    """
    Reads a UTF8 text file and prints its content to stdout.

    The function opens the file with the given filename,
    reads the file content,
    and then prints it to the standard output. It uses the 'with' statement
    for file handling, which automatically takes care of closing the file
    after it is no longer needed.

    Args:
        filename (str): The name of the file to read.
        Default is an empty string.

    Returns:
        None.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
