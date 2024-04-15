#!/usr/bin/python3
"""inherit the list class"""


class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()
    """defines a func to print this list sorted"""
    def print_sorted(self):
        print(sorted(self))
