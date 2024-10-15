#!/usr/bin/python3
"""Module for 9-rectangle.py
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle inherit from BaseGeomtry """

    def __init__(self, width, height):
        """ Constructor """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Returns area of Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """ string repr of Rectangle object """
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)i
