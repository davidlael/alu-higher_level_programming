#!/usr/bin/python3
"""
Module 4-inherits_from
Defines a function that checks subclass inheritance.
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited from a_class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        bool: True if obj inherited (directly or indirectly) from a_class,
              False if it is an exact instance of a_class or not inherited.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
