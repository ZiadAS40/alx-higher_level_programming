#!/bin/bash
# sends a GET request and then diplay the body of the response only if staus code is 200.
curl -sL "$1"
