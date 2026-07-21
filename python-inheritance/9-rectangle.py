#!/usr/bin/python3
"""
Module 9-rectangle
Defines a class Rectangle that inherits from BaseGeometry with area and str.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle class inherited from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: Area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the Rectangle.

        Returns:
            str: Description format '[Rectangle] <width>/<height>'.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
