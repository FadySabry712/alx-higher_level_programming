#!/usr/bin/python3
'''Module for 2-is_same_class method.'''


def is_same_class(obj, a_class):
    '''Determines if object is exactly an instance of a class.'''
    return type(obj) == a_class
