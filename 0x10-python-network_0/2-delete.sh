#!/bin/bash
# DELETE request passed as 1st arg and displays body of the reponse
curl -s "$1" -X DELETE