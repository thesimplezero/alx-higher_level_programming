#!/usr/bin/python3
"""
Sends request to URL, handles HTTP errors, and displays response body.
"""

import urllib.request
import urllib.error
import sys


def fetch_and_display(url):
    """
    Send request to URL, handle HTTP errors, and display response body.

    Args:
        url (str): URL to send request to.
    """
    try:
        with urllib.request.urlopen(url) as response:
            # Read and decode response body
            body = response.read().decode('utf-8')

            # Print response body
            print(body)
    except urllib.error.HTTPError as e:
        # Handle HTTP errors gracefully
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./3-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_and_display(url)
