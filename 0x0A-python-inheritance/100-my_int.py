#!/usr/bin/python3
"""
This module defines a class 'MyInt' that inherits
from 'int' and inverts the '==' and '!=' operators.
"""


class MyInt(int):
    """
    A subclass that inherits from 'int'.
    This class inverts the behaviour of the '==' and '!=' operators.
    """

    def __eq__(self, value):
        """
        Override '==' operator to behave as '!='.

        Parameters:
            value (int): The integer value to
            compare with the 'MyInt' instance.

        Returns:
            bool: The inverted result of the '==' comparison.
        """
        return self.real != value

    def __ne__(self, value):
        """
        Override '!=' operator to behave as '=='.

        Parameters:
            value (int): The integer value to
            compare with the 'MyInt' instance.

        Returns:
            bool: The inverted result of the '!=' comparison.
        """
        return self.real == value
