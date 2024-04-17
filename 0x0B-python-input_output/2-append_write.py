#!/usr/bin/python3
"""using the with statement"""


def append_write(filename="", text=""):
    """append the text the end of a file"""
    with open(filename, "a", encoding="utf-8") as file:
        result = file.write(text)
    return result
