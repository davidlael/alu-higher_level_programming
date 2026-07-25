#!/usr/bin/python3
"""Module that contains a function that adds two integers."""


def add_integer(a, b=98):
    """Adds two integers or floats casted to integers.

    Args:
        a: First number (int or float).
        b: Second number (int or float).

    Returns:
        The integer sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a != a:
        raise ValueError("cannot convert float NaN to integer")
    if b != b:
        raise ValueError("cannot convert float NaN to integer")
    return int(a) + int(b)
