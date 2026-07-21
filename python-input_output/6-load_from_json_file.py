#!/usr/bin/python3
"""
Module 6-load_from_json_file
Contains a function that creates an Object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file.

    Args:
        filename (str): The JSON file path to read from.

    Returns:
        object: Python object deserialized from JSON.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
