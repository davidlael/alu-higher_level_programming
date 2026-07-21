#!/usr/bin/python3
"""
Module 4-from_json_string
Contains a function that returns an object represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to deserialize.

    Returns:
        object: Python data structure represented by my_str.
    """
    return json.loads(my_str)
