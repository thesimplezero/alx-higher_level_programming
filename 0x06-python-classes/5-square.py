#!/usr/bin/python3
"""This module defines a class Square representing a geometric square."""


class Square:
    """Represent a geometric square."""

    def __init__(self, size=0):
        """Initialize a new square and set size with validation.
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
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

    def my_print(self):
        """Print the square using the '#' character."""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                for _ in range(self.__size):
                    print("#", end="")
                print("")
