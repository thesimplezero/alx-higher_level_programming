#!/bin/bash

# Check if the URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Use cURL to send a request to the URL and save the response body to a temporary file
response=$(curl -sI "$1" | grep -i 'Content-Length' | awk '{print $2}' | tr -d '\r')
echo "$response"
