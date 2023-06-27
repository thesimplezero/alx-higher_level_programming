#!/usr/bin/python3
"""Module defines a Square class representing a square shape."""


class Square:
    """Represents a geometric square, with validation on size."""

    def __init__(self, size=0):
        """Initialize square, validate and set the size.
        Args:
            size (int): The size of the new square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate and return the current area of the square."""
        return (self.__size * self.__size)
