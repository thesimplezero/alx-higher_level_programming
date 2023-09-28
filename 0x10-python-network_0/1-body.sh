#!/bin/bash

# Check if the URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Use cURL to send a GET request to the URL and display the body if the response code is 200
response_code=$(curl -s -o /dev/null -w "%{http_code}" -L "$1")
if [ "$response_code" -eq 200 ]; then
    curl -s -L "$1"
else
    echo "Response code: $response_code"
fi
