#!/usr/bin/python3
"""
This script takes command line arguments and saves them as a JSON list
in a file named 'add_item.json'. If the file does not exist, it is created.

The script uses the 'save_to_json_file' function from '5-save_to_json_file.py'
and the 'load_from_json_file' function from '6-load_from_json_file.py'. The
file permissions or exceptions are not managed in this script.
"""

import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
