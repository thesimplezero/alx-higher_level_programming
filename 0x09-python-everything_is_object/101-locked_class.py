#!/usr/bin/python3
"""Provides a class with a fixed attribute set."""


class LockedClass:
    """
    This class restricts the instantiation of new attributes,
    only allowing for the 'first_name' attribute to be created.
    """

    __slots__ = ["first_name"]
