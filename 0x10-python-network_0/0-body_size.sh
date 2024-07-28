#!/bin/bash
# displays the size of the response.
curl -Is "$1" | grep -i "Content-Length" | awk '{print $2}'
