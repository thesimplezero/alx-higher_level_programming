#!/usr/bin/python3

def remove_char_at(str, n):
    """Create a copy of the string without the character at position n."""
    return str if n < 0 else str[:n] + str[n+1:]
