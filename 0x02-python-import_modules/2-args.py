#!/usr/bin/python3
import sys

def main():
    """Print the number of and list of arguments."""
    arg_count = len(sys.argv) - 1

    # Using f-string for more readability
    if arg_count == 0:
        print("0 arguments.")
    elif arg_count == 1:
        print("1 argument:")
    else:
        print(f"{arg_count} arguments:")

    for index, argument in enumerate(sys.argv, start=1):
        print(f"{index}: {argument}")

if __name__ == "__main__":
    main()
