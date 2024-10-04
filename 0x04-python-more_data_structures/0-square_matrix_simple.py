#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_list = []
    for i in matrix:
        squared = list(map(lambda x: x ** 2, i))
        squared_list.append(squared)
    return squared_list
