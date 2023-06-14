#!/usr/bin/python3
def roman_to_int(roman_string):
    """Convert a Roman numeral to an integer."""
    # Return 0 if the input is not a string
    if not isinstance(roman_string, str):
        return 0

    # Define the roman numerals mapping
    romans = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    # Create a list of integer values
    values = [
        romans[i] if romans[i] >= romans[j] else -romans[i]
        for i, j in zip(roman_string, roman_string[1:])
    ]

    # Return the sum of the values, adding the last roman numeral
    return sum(values) + romans[roman_string[-1]]
