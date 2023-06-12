#!/usr/bin/python3
def no_c(my_string):
    """Function that removes all c and C characters from a string"""
    new_string = ''.join(ch for ch in my_string if ch not in 'cC')
    return new_string
