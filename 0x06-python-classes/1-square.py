#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """
    Class that defines properties of square by: (based on 0-square.py).

    Attributes:
        size: size of a square.
    """
    def __init__(self, size):
        """Creates instances of square (1 side).

        Args:
            size: size of the square.
        """
        self.__size = size
