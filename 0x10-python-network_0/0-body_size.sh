#!/bin/bash

# Check if the number of arguments is correct
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url="$1"

# Use curl to send a request and display the size of the body in bytes
curl -sI "$url" | grep -i Content-Length | awk '{print $2}' | tr -d '\r\n'
