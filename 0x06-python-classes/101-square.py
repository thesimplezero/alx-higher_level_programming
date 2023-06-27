#!/usr/bin/python3
"""
This module defines a Square class that models a geometric square with a
specified size and position. The size and position attributes have
appropriate getter and setter methods with validations. The class also
includes methods to compute the area and print the square.
"""


class Square:
    """
    A geometric square with a certain size and position. The size and position
    are integers. Provides methods for computing the area and printing the
    square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square with size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the Square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the Square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position with validation."""
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character # using position."""
        if self.__size == 0:
            print()
        else:
            print('\n' * self.__position[1], end="")
            for i in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)

    def __str__(self):
        """Define the print() representation of a Square instance."""
        if self.__size == 0:
            return ''
        return ('\n' * self.__position[1] +
                '\n'.join(' ' * self.__position[0] + '#' * self.__size
                          for _ in range(self.__size)))
