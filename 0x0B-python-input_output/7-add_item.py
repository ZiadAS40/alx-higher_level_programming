#!/usr/bin/python3
"""
a script to get all the arguments
from the command line and convert
it to json string and save it on
a file and then load this from the
file and print it
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
filename = "add_item.json"

try:
    myList = load_from_json_file(filename)
except FileNotFoundError:
    myList = []

for arg in sys.argv[1:]:
    myList.append(arg)

save_to_json_file(myList, filename)
