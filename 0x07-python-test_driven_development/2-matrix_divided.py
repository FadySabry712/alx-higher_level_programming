#!/usr/bin/python3
"""Module for matrix_divided method."""


def matrix_divided(matrix, div):

    """Divides all elements of matrix by div.
    Arguments:
        matrix: List containing int or float
        div: num to divide matrix by
    Return:
        list: List representing divided matrix.
    Raise:
        TypeError: If matrix is not list containing int or float.
        TypeError: If sublist are not all same size.
        TypeError: If div is not int or float.
        ZeroDivisionError: If divison is zero.
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(x / div, 2) for x in row] for row in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
