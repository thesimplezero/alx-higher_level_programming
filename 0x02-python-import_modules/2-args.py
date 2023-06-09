#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    count = len(sys.argv) - 1
    args_message = {
        0: "0 arguments.",
        1: "1 argument:"
    }

    print(args_message.get(count, f"{count} arguments:"))

    for i in range(count):
        print(f"{i + 1}: {sys.argv[i + 1]}")
