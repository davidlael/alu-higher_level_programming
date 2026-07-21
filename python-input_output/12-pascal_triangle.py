#!/usr/bin/python3
"""
Module 12-pascal_triangle
Returns a list of lists representing Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle of size n.

    Args:
        n (int): Number of rows in Pascal's triangle.

    Returns:
        list: List of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev = triangle[-1]
        row = [1]
        for j in range(len(prev) - 1):
            row.append(prev[j] + prev[j + 1])
        row.append(1)
        triangle.append(row)

    return triangle
