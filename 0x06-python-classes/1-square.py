#!/usr/bin/python3
"""Define a square class"""

class Square:
    """
    a class Square that defines a square by: (based on 0-square.py)

    Private instance attribute: size
    """
    def __init__(self, size):
    """
    craete new instance of a square size
    
    Args:
        size: length of aside of a squre
    """
        self.__size = size
