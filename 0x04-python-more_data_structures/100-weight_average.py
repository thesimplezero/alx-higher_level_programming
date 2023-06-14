#!/usr/bin/python3
def weight_average(my_list=[]):
    """Returns the weighted average of all integer tuples (<score>, <weight>)."""
    if not my_list:
        return 0

    num = sum(score * weight for score, weight in my_list)
    den = sum(weight for _, weight in my_list)

    return num / den
