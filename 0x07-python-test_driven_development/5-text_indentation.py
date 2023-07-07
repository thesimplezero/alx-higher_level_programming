#!/usr/bin/python3
"""Module that defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', ':'

    Args:
        text (string): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ".?:"
    text = text.strip()
    i = 0
    while i < len(text):
        print(text[i], end='')
        if text[i] in special_chars:
            print('\n')
            if i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        i += 1
