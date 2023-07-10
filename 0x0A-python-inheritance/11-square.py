#!/usr/bin/python3
"""
This module defines a class 'Square' that inherits
from 'Rectangle' (9-rectangle.py).
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A subclass that inherits from 'Rectangle'.
    This class represents a square.
    """

    def __init__(self, size):
        """
        Initialize a new Square instance.

        Parameters:
            size (int): The size of the new Square.
            It represents both the width and height of the Square,
            since width and height are equal in a square.
            It must be a positive integer.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not greater than 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Return the print() and str() representation of
        a Square in the format: [Square] <width>/<height>.
        """
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
