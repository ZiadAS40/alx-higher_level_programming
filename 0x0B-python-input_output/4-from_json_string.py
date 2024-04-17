#!/usr/bin/python3
"""using the import"""
import json


def from_json_string(my_str):
    """it loads an object from a json string
    and then return it
    """
    return json.loads(my_str)
