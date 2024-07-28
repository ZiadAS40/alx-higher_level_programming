#!/bin/bash
# displays the options that the server accept
curl -s -I -X OPTIONS "$1" | grep -i "Allow:" | cut -d' ' -f2-
