#!/usr/bin/python3
def uniq_add(my_list=None):
    """Adds all unique integers in a list (only once for each integer)."""
    if my_list is None:
        my_list = []
    return sum(set(my_list))
