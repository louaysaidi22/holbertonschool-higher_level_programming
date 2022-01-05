#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squaredmatrix = list.copy(matrix)
    for i in range(len(matrix)):
        squaredmatrix[i] = [n ** 2 for n in matrix[i]]
    return squaredmatrix
