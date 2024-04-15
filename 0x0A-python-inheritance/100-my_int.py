#!/usr/bin/python3
"""
MyInt class
"""


class MyInt(int):
    """rebel version of an integer"""
    def __new__(cls, *args, **kwargs):
        """create a new instance"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """equal"""
        return int(self) != other

    def __ne__(self, other):
        """not equal"""
        return int(self) == other
