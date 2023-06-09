#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
import sys


def main():
    operators = {"+": add, "-": sub, "*": mul, "/": div}

    if len(sys.argv) != 4 or sys.argv[2] not in operators:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a, b = map(int, (sys.argv[1], sys.argv[3]))
    print(f"{a} {sys.argv[2]} {b} = {operators[sys.argv[2]](a, b)}")


if __name__ == "__main__":
    main()
