#!/usr/bin/python3
"""
Retrieves data from the URL and displays details about the response.
"""

import urllib.request


def fetch_url_data(url):
    """
    Retrieve data from the URL and output information regarding the response.

    Args:
        url (str): URL to fetch data from.
    """
    try:
        with urllib.request.urlopen(url) as response:

            content = response.read()
            utf8_content = content.decode('utf-8')

            # Print information
            print("Body response:")
            print(f"    - type: {type(content)}")
            print(f"    - content: {content}")
            print(f"    - utf8 content: {utf8_content}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    fetch_url_data(url)