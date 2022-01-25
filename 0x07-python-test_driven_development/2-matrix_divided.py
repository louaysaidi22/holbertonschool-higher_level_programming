#!/usr/bin/python3
"""task1"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix"""
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    elif not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    dividedmatrix = []
    row_len = len(matrix[0])
    for i in range(len(matrix)):
        if len(matrix[i]) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for j in range(row_len):
            if not isinstance(
                    matrix[i][j],
                    int) and not isinstance(
                    matrix[i][j],
                    float):
                raise TypeError(
                    "matrix must be a matrix (list of lists)"
                    " of integers/floats")
            new_row.append(round(matrix[i][j] / div, 2))
        dividedmatrix.append(new_row)
    return dividedmatrix
