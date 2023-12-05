#!/bin/bash
# This script takes in a URL, sends a GET request to the URL, and displays the body of the response for a 200 status code
curl -s "$1" -X GET -i | awk '/HTTP\/1.0 200 OK/{flag=1; next} flag; /./{flag=0}'
