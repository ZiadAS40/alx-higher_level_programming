#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for j in matrix:
        for i in j:
            print("{}".format(i), end=' ')
        print("$")
