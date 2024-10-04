#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_list = []

    for i in matrix:
        squared_res = list(map(lambda x: x **2, i))
        square_list.append(squared_res)
    return square_list
