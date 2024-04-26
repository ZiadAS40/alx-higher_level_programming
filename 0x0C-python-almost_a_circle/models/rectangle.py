#!/usr/bin/python3
"""The Rectangle class inherits from the Base class"""
from models.base import Base


class Rectangle(Base):
    """Define the Rectangle class inheriting from the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle instance with width,height, x and y coordinates.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle.Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle.Defaults to 0.
            id (optional): An optional id of the rectangle. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getting the width attr"""
        return self.__width

    @width.setter
    def width(self, value):
        """getting the width attr"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getting the height attr"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting the height attr"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getting the x attr"""
        return self.__x

    @x.setter
    def x(self, value):
        """setting the x attr"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getting the y attr"""
        return self.__y

    @y.setter
    def y(self, value):
        """setting the y attr"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """get the area of the class"""
        return self.width * self.height

    def display(self):
        """display simple info about the class"""
        print("\n" * self.y, end='')
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """print the class in proper way"""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Update the Rectangle.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args:
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        else:
            for key in kwargs:
                if key in attributes:
                    setattr(self, key, kwargs[key])
