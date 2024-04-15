#!/usr/bin/python3
"""inherit the list class"""


class MyList(list):
    """defines a func to print this list sorted"""
    def print_sorted(self):
        print(sorted(self))
