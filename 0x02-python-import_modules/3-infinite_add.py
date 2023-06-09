#!/usr/bin/python3

if __name__ == "__main__":
    """add infinite number on cLD arg"""
    import sys

    argv = sys.argv
    total = sum(int(i) for i in argv[1:])
    print(total)
