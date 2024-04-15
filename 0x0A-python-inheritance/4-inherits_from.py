#!/usr/bin/python3
"""checks if it is only a subclass"""


def inherits_from(obj, a_class):
    """perform the checks"""
    if isinstance(obj, a_class):
        return type(obj) != a_class
    return False
