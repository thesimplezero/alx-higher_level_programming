#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        result = ('Fizz' * (x % 3 == 0) + 'Buzz' * (x % 5 == 0)) or x
        print("{} ".format(result), end="")
