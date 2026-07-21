#!/usr/bin/python3
"""
Module 5-save_to_json_file
Contains a function that writes an Object to a text file using JSON.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj: The object to serialize and save.
        filename (str): The file path where JSON is saved.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
