#!/usr/bin/python3
"""using the with statement"""


def read_file(filename=""):
    """read a file and print it"""
    with open(filename, "r", encoding="utf-8") as file:
        result = file.read()
        print(result, end='')
