#!/usr/bin/python3
"""inherit the list class"""


class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """defines a func to print this list sorted"""
        print(sorted(self))
