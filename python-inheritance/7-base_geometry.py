#!/usr/bin/python3
"""
Module 7-base_geometry
Defines a class BaseGeometry with area method and integer validator.
"""


class BaseGeometry:
    """A BaseGeometry class with area calculation and value validation."""

    def area(self):
        """
        Raises an Exception indicating area is not implemented.

        Raises:
            Exception: Always raises Exception with message
            'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a given value is a positive integer.

        Args:
            name (str): The name associated with the value.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
