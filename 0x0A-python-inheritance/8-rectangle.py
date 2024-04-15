#!/usr/bin/python3
"""creat an instance of the class geometry"""


class Rectangle(BaseGeometry):
    """an instance of the BaseGeometry class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
