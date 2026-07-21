#!/usr/bin/python3
"""
Module 3-is_kind_of_class
Defines a function that checks if an object is an instance of a class
or a class inherited from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or inherited from, a class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        bool: True if obj is an instance or inherited instance,
              False otherwise.
    """
    return isinstance(obj, a_class)
