#!/usr/bin/python3

# Single print function with one loop in a generator expression
print("".join(chr(i) for i in range(ord('a'), ord('z')+1)), end="")
