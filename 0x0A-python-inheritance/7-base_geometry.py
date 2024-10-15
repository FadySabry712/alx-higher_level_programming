#!/usr/bin/python3
"""Module for BaseGeometry.
"""


class BaseGeometry():
    """BaseGeometry Class"""

    def area(self):
        """Raise Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value"""
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
