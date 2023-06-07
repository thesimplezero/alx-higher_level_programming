#!/usr/bin/python3
"""
Print the ASCII alphabet in reverse order.

Alphabet letters are printed in alternating upper- and lower-case.
"""
# Loop through ASCII values for z to a (122 to 97)
for ascii_value in range(122, 96, -1):
    # If ASCII value is even, print lowercase. If odd, print uppercase
    print("{:c}".format(
        ascii_value if ascii_value % 2 == 0 else ascii_value - 32), end="")
