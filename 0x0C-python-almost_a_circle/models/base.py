#!/usr/bin/python3
"""the base Class"""


class Base:
    """define the base class with the
    bultin __init___ and the private
    attr __nb_objects"""

    
    __nb_objects = 0

    def __init__(self, id=None):
        self.__nb_objects += 1
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @property
    def nb_objects(self):
        return self.__nb_objects
    
    @nb_objects.setter
    def nb_objects(self, value):
        self.__nb_objects = value
    