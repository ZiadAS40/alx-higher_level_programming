#!/usr/bin/python3
"""function that get a json representation from a file"""
import json


def load_from_json_file(filename):
    """
    deserialize a json string and return it
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
