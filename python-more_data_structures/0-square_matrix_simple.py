#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        new_list = []
        for j in i:
            new_list.append(j**2)
        new_matrix.append(new_list)
    return new_matrix
