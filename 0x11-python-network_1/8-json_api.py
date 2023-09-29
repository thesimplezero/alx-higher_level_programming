#!/usr/bin/python3
"""
Sends POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter.
"""

import requests
import sys

# Constants
URL = 'http://0.0.0.0:5000/search_user'
CONTENT_TYPE_JSON = 'application/json'

def search_user(letter):
    """
    Sends a POST request to search for a user based on a letter.

    Args:
        letter (str): Letter to search for.
    """
    try:
        if not letter:
            print("Please provide a letter as an argument.")
            return

        # Define parameters
        params = {'q': letter}

        # Send POST request
        response = requests.post(URL, data=params)
        response.raise_for_status()  # Check HTTP errors

        # Check if response has valid JSON data
        if response.headers.get('content-type') == CONTENT_TYPE_JSON:
            data = response.json()

            # Check if JSON data is not empty
            if data:
                print(f"[{data['id']}] {data['name']}")
            else:
                print("No result")
        else:
            print("Not a valid JSON")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Error: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request Error: {req_err}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./search_user.py <letter>")
        sys.exit(1)

    letter = sys.argv[1]  # Letter provided as the first command-line argument
    search_user(letter)
