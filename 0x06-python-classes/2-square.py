#!/usr/bin/python3
"""Module defining Square class, representing a geometric square."""


class Square:
    """Represents a square, with validation on size type and value."""

    def __init__(self, size=0):
        """Initialize square, validate and set the size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
