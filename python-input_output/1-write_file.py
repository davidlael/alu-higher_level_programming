#!/usr/bin/python3
"""
Module 1-write_file
Contains a function that writes a string to a text file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns character count.

    Args:
        filename (str): The path to the file. Defaults to "".
        text (str): The text to write. Defaults to "".

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
