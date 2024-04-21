#!/usr/bin/python3
from models.base import Base
"""the rectangle class inherts from the Base class"""


class Rectangle(Base):
    """define the rectangle class inerting from the
    Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    def area(self):
        return self.width *self.height
    
    def display(self):
        for i in range(self.y):
            print()
        for i in range(self.height):
            for i in range(self.x):
                print(' ', end='')
            for n in range(self.width):
                print("#", end='')
            print()
    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)
    def update(self, *args):
        if args[0] is not None:
            self.id = args[0]
        if len(args) > 1:
            if args[1] is not None:
                self.width = args[1]
        if len(args) > 2:
            if args[2] is not None:
                self.height = args[2]
        if len(args) > 3:
            if args[3] is not None:
                self.x = args[3]
        if len(args) > 4:
            if args[4] is not None:
                self.y = args[4]
        
    