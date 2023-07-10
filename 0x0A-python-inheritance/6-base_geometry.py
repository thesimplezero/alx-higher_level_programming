#!/usr/bin/python3
"""
This module provides a 'BaseGeometry' class
"""


class BaseGeometry:
    """
    A BaseGeometry class that provides an unimplemented 'area' method
    """

    def area(self):
        """
        Raises an Exception with a message that the method is not implemented

        Raises:
            Exception: Always, as this method is not yet implemented
        """
        raise Exception("area() is not implemented")
