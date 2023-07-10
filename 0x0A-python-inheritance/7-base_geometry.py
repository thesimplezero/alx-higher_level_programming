#!/usr/bin/python3
"""
This module defines a class 'BaseGeometry' that includes methods for
validating and raising exceptions for unimplemented methods.
"""


class BaseGeometry:
    """
    A class that provides an unimplemented method 'area' and a method to
    validate integers 'integer_validator'.
    """

    def area(self):
        """
        Raises an Exception with a message that the method is not implemented.

        Raises:
            Exception: Always, as this method is not yet implemented.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates that 'value' is a positive integer.

        Args:
            name (str): The name associated with 'value'.
            value (int): The value to validate.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
