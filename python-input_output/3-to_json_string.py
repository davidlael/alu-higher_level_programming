#!/usr/bin/python3
"""
Module 3-to_json_string
Contains a function that returns the JSON representation of an object.
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to serialize into JSON.

    Returns:
        str: JSON representation of my_obj.
    """
    return json.dumps(my_obj)
