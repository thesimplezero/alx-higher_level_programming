#!/usr/bin/python3
"""
Retrieve the X-Request-Id variable from the header of the URL response.
"""

import urllib.request
import sys


def fetch_x_request_id(url):
    """
    Retrieve the X-Request-Id variable from the header of the URL response.

    Args:
        url (str): URL to send request to.
    """
    try:
        # Create request and open URL
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            # Check if 'X-Request-Id' header exists in response
            if 'X-Request-Id' in response.headers:
                x_request_id = response.headers['X-Request-Id']
                print(x_request_id)
            else:
                print("X-Request-Id not found in the response headers.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_x_request_id(url)
