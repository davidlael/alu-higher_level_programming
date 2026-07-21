#!/usr/bin/python3
"""
Module 10-student
Defines a class Student with filtered JSON representation.
"""


class Student:
    """Defines a student object."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): First name of student.
            last_name (str): Last name of student.
            age (int): Age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): List of string attributes to retrieve.

        Returns:
            dict: Dictionary representation containing selected attributes.
        """
        if (type(attrs) is list and
                all(type(item) is str for item in attrs)):
            res = {}
            for k, v in self.__dict__.items():
                if k in attrs:
                    res[k] = v
            return res
        return self.__dict__
