#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 and len(matrix[0]) == 0:
        print("")
    else:
        for i in matrix:
            for n in i:
                if n != i[-1]:
                    print("{:d}".format(n), end=" ")
                else:
                    print("{:d}".format(n))
