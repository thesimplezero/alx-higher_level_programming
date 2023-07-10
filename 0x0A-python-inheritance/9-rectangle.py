#!/usr/bin/python3
"""
This module defines a class 'Rectangle' that inherits from
'BaseGeometry' (7-base_geometry.py).
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
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Return the area of the rectangle instance.
        The area is the product of width and height.

        Returns:
            The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the print() and str() representation of the Rectangle instance.
        It is in the format '[Rectangle] <width>/<height>'.

        Returns:
            The string representation of the rectangle instance.
        """
        return "[{}] {}/{}".format(self.__class__.__name__, self.__width, self.__height)
