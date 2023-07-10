#!/usr/bin/python3
"""
This module contains the MyList class that inherits from list
The MyList class includes a method to print the list in ascending order
"""


class MyList(list):
    """
    The MyList class inherits from list and includes a method to print
    the list in ascending order
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order
        This does not modify the original list
        """
        print(sorted(self))
