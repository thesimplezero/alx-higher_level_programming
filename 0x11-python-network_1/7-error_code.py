#!/usr/bin/python3
"""
Sends request to URL and displays body of response.
If HTTP status code is greater than or equal to 400,
it prints an error message.
"""

import requests
import sys


def fetch_url(url):
    """
    Fetches URL and handles HTTP status codes.

    Args:
        url (str): URL to send request to.
    """
    try:
        response = requests.get(url)

        # Check the HTTP status code
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
        else:
            print(response.text)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Error: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request Error: {req_err}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./fetch_url.py <URL>")
        sys.exit(1)

    url = sys.argv[1]  # URL provided as the first command-line argument
    fetch_url(url)
