#!/usr/bin/python3
""" Module for 4-inherits_from.py
"""


def inherits_from(obj, a_class):
    """ Check for inheritance """
    if (type(obj) != a_class):
        return isinstance(obj, a_class)
    return False
