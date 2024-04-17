#!/usr/bin/python3
"""using import"""
import json


def save_to_json_file(my_obj, filename):
    """it serialize an object and save it on a file(filename)"""
    with open(filename, "r", encoding="utf-8") as file:
        json.dump(my_obj, file)
