#!/usr/bin/python3
"""using the with statement"""


def write_file(filename="", text=""):
    """write into a file and return it"""
    with open(filename, "w", encoding="utf-8") as file:
        result = file.write(text)
    return result
