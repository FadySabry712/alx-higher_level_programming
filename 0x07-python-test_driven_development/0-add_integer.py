#!/usr/bin/python3
"""Module for Add Integer method."""


def add_integer(a, b=98):
    """Adds two integers.

    Arguments:
        a: the first integer.
        b: the second integer, default 98.

    Raise:
        TypeError: if a, b are not int, float.

    Return:
        The sum of the two int.
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
