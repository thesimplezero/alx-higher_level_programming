#!/usr/bin/python3
"""
This module defines a Square class that models a geometric square with a
specified size. The size attribute has appropriate getter and setter
methods with validations. The class also includes a method to compute
the area and implements comparison methods based on the square area.
"""


class Square:
    """
    A geometric square with a certain size, which can be an integer or a float.
    Provides methods for computing the area and comparison methods
    based on the area.
    """

    def __init__(self, size=0):
        """Initialize a new Square with size."""
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the Square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Define the == comparison to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return not self == other

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self == other or self < other

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return not self <= other

    def __ge__(self, other):
        """Define the >= comparison to a Square."""
        return not self < other
