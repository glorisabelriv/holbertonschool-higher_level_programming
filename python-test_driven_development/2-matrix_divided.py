#!/usr/bin/python3


def matrix_divided(matrix, div):

    """Divide a Matrix by two
    """
    if not isinstance(matrix, list):
        raise TypeError
        ("matrix must be a matrix (list of lists) of integers/floats")
    size = None
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError
        ("matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(row)
        elif size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row] for row in matrix]
