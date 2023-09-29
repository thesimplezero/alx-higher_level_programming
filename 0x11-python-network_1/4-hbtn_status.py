#!/usr/bin/python3
"""
Fetches data from URL and displays response body.
"""

import requests


def fetch_url_data(url):
    """
    Fetch data from URL and display response body.

    Args:
        url (str): URL to fetch data from.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check HTTP errors

        # Print response body
        print("Body response:")
        print(f"\t- type: {type(response.text)}")
        print(f"\t- content: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    fetch_url_data(url)
