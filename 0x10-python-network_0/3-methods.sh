#!/bin/bash
# displays the options that the server accept
curl -s -X OPTIONS "$1"
