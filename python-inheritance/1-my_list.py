#!/usr/bin/python3
"""
Module 1-my_list
Defines a class MyList that inherits from list.
"""


class MyList(list):
    """A subclass of list that adds sorted printing capability."""

    def print_sorted(self):
        """Prints the list in ascending sorted order without modifying it."""
        print(sorted(self))
