#!/usr/bin/python3
"""
This module defines a 'Student' class.

The Student class defines a student by first name, last name, and age.
It includes an instance method 'to_json' that retrieves a dictionary
representation of a Student instance with optional attribute filtering.
No module is imported in this script.
"""


class Student:
    """
    Defines a student with first name, last name, and age attributes.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Parameters:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If 'attrs' is a list of strings, only attributes included in the list
        are retrieved. Otherwise, all attributes are retrieved.

        Parameters:
        attrs (list): A list of attributes to retrieve.

        Returns:
        dict: A dictionary representation of the Student instance.
        """
        if isinstance(attrs, list) and all(isinstance(ele, str) for ele in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__
