#!/bin/bash
#Takes in a URL and send a request to it
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'