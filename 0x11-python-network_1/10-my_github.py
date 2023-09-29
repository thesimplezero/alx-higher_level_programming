#!/usr/bin/python3
"""
Displays GitHub user ID using GitHub API and Basic Authentication.
"""

import requests
import sys

# Constants
API_URL = 'https://api.github.com/user'

def get_github_id(username, password):
    """
    Retrieves and displays GitHub user ID using Basic Authentication.

    Args:
        username (str): GitHub username.
        password (str): Personal access token.

    Returns:
        int: Your GitHub user ID.
    """
    try:
        if not username or not password:
            print("Please provide both a username and a password.")
            return

        # Create a Basic Authentication session
        session = requests.Session()
        session.auth = (username, password)

        # Send GET request to GitHub API
        response = session.get(API_URL)
        response.raise_for_status()  # Check HTTP errors

        # Check if the response is successful (HTTP status code 200)
        if response.status_code == 200:
            # Parse JSON response and get the user ID
            user_data = response.json()
            github_id = user_data['id']
            print(github_id)
        else:
            # Print None if the request was not successful
            print(None)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Error: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request Error: {req_err}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./get_github_id.py <username> <password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    get_github_id(username, password)
