#!/usr/bin/python3
"""
Module 1-square
Defines a class Square with a private instance attribute size.
"""


class Square:
    """Defines a square with a private size attribute."""

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size: The size of the square (no type validation yet).
        """
        self.__size = size
