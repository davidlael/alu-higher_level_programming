#!/usr/bin/python3
"""
Module 6-base_geometry
Defines a class BaseGeometry with an unimplemented area method.
"""


class BaseGeometry:
    """A BaseGeometry class with area calculation placeholder."""

    def area(self):
        """
        Raises an Exception indicating area is not implemented.

        Raises:
            Exception: Always raises Exception with message
            'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
