#!/usr/bin/python3
"""Module for dividing all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div.

    Args:
        matrix: List of lists of integers or floats.
        div: Number (int or float) to divide matrix elements by.

    Returns:
        A new matrix with rounded results.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        for elem in row:
            if not isinstance(elem, (int, float)) or elem != elem:
                raise TypeError(msg)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)) or div != div:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
