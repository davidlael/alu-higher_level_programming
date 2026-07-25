#!/usr/bin/python3
"""Module for dividing all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a divisor.

    Args:
        matrix: A list of lists of integers or floats.
        div: The number (int or float) to divide elements by.

    Returns:
        A new matrix with elements rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is invalid or rows are of different sizes.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(msg)

    for row in matrix:
        if not isinstance(row, list) or not row:
            raise TypeError(msg)
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(msg)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
