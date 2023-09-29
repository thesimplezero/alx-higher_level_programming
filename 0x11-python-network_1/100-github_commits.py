#!/usr/bin/python3
"""using GitHub API to list commits"""

import sys
import requests


if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        owner_name, repository_name)

    params = {'per_page': 10}

    # send a GET request to the GitHub API
    response = requests.get(url, params=params)

    # parse the JSON response
    commits = response.json()
    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
