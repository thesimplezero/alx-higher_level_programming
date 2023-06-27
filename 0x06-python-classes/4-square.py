#!/usr/bin/python3
"""This module defines a class Square representing a geometric square."""


class Square:
    """Represents a geometric square with validation and area calculation."""

    def __init__(self, size=0):
        """Initialize a new square and set size with validation.
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """int: The size of the square which is always non-negative."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation.
        Args:
            value (int): The size of the square.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the current area of the square."""
        return self.__size * self.__size
