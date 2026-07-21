#!/usr/bin/python3
"""
Module 0-read_file
Contains a function that reads a text file and prints it to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its contents to standard output.

    Args:
        filename (str): The path to the file to be read. Defaults to "".
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
