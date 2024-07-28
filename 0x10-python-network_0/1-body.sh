#!/usr/bin/env bash
# sends a GET request and then diplay
#+ the body of the response only if
#+staus code is 200.
response=$(curl -s -I -X GET "$1" | head -n 1 | awk '{print $2}')
if [[ $response -eq 200 ]]; then
        echo $(curl -s -X GET "$1")
fi
