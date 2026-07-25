#!/usr/bin/python3
"""Module that prints a square with the '#' character."""


def print_square(size):
    """Prints a square with size length using '#' character.

    Args:
        size: Size length of the square (int).
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
