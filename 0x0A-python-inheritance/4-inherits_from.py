#!/usr/bin/python3
"""Module for 4-inherits_from.py
"""


def inherits_from(obj, a_class):
    """ Check for inheritance of a class from true subclass 
    """
    return isinstance(obj, a_class) and type(obj) != a_class
