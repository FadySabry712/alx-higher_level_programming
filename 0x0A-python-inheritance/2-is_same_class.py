#!/usr/bin/python3
"""Module for 2-is_same_class.py
"""


def is_same_class(obj, a_class):
    """ See if object is exactly an instance of a_class """
    return type(obj) == a_class
