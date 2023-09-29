#!/usr/bin/python3
"""
Send a POST request to the URL with an email parameter and
then display the response body.
"""

import urllib.request
import urllib.parse
import sys


def send_post_request(url, email):
    """
    Send a POST request to the URL with an email parameter and
    then display the response body.

    Args:
        url (str): URL to send request to.
        email (str): The email to send as parameter.
    """
    try:
        # Create dictionary with email parameter
        data = {'email': email}
        data = urllib.parse.urlencode(data).encode('utf-8')

        req = urllib.request.Request(url, data)
        with urllib.request.urlopen(req) as response:
            # Read and decode response body
            body = response.read().decode('utf-8')

            # Print response body
            print(body)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    send_post_request(url, email)
