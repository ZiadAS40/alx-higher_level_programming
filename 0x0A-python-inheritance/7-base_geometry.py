#!/usr/bin/python3
"""
a geometry class
"""


class BaseGeometry:
    """now adds validating func"""
    def area(self):
        raise Exception("area() is not implemented")

    """intger validator"""
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be an integer".format(name))
