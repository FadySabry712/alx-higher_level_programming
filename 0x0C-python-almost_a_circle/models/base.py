#!/usr/bin/python3
""" Module for the Base clas """


class Base:
    """ this is the intiliazion of Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        this is the constructor method of the Base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
