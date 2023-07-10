#!/usr/bin/python3
"""
This module defines a class 'Rectangle' that inherits
from 'BaseGeometry' (7-base_geometry.py).
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A subclass that inherits from 'BaseGeometry'.
    This class represents a rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance.

        Parameters:
            width (int): The width of the new Rectangle instance.
            It must be a positive integer.
            height (int): The height of the new Rectangle instance.
            It must also be a positive integer.

        Raises:
            TypeError: If width or height are not integers.
            ValueError: If width or height are not greater than 0.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
