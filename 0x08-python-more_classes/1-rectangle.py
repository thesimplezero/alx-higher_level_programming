#!/usr/bin/python3
"""
This module defines a Rectangle class.
"""


class Rectangle:
    """
    This class represents a rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle.

        Parameters:
        width (int): The width of the new rectangle.
        height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the Rectangle.

        Parameters:
        value (int): The width of the rectangle.

        Raises:
        TypeError: If `value` is not an integer.
        ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the Rectangle.

        Parameters:
        value (int): The height of the rectangle.

        Raises:
        TypeError: If `value` is not an integer.
        ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
