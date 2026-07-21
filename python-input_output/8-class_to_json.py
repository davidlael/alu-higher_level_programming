#!/usr/bin/python3
"""
Module 8-class_to_json
Contains a function that returns dictionary description for JSON.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: The dictionary description of obj attributes.
    """
    return obj.__dict__
