#!/usr/bin/python3
"""
Module 10-square
Defines a class Square that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class inherited from Rectangle."""

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): Size of the square sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
