#!/usr/bin/python3
"""
Module 2-square
Defines a class Square with type and value validation for size.
"""


class Square:
    """Defines a square with validated size attribute."""

    def __init__(self, size=0):
        """
        Initializes a new Square instance with size validation.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
