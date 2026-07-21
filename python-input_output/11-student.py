#!/usr/bin/python3
"""
Module 11-student
Defines a class Student with reload capability from JSON dictionary.
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
            attrs (list, optional): List of attribute names to retrieve.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if (type(attrs) is list and
                all(type(item) is str for item in attrs)):
            res = {}
            for k, v in self.__dict__.items():
                if k in attrs:
                    res[k] = v
            return res
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance using a dict.

        Args:
            json (dict): Dictionary with key/value attribute updates.
        """
        for k, v in json.items():
            setattr(self, k, v)
