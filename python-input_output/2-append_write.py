#!/usr/bin/python3
"""
Module 2-append_write
Contains a function that appends a string to the end of a text file.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8).

    Args:
        filename (str): The path to the file. Defaults to "".
        text (str): The text to append. Defaults to "".

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
