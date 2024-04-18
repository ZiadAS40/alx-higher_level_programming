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

    def to_json(self, attrs=None):
        """retrives a dictionary representation of the
        Student Class
        """
        if attrs is not None and all(isinstance(attr, str) for attr in attrs):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        else:
            return self.__dict__
        
    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
