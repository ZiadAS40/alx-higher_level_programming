#!/usr/bin/python3
"""Stuent class"""


class Student():
    """defines the __init__ and
    to_json() functions
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrives a dictionary representation of the
        Student Class
        """
        return self.__dict__
