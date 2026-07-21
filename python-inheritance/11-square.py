#!/usr/bin/python3
"""
Module 11-square
Defines a class Square that inherits from Rectangle with custom str.
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

    def __str__(self):
        """
        Returns a string representation of the Square.

        Returns:
            str: Description format '[Square] <width>/<height>'.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
