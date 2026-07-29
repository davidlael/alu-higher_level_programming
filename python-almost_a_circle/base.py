#!/usr/bin/python3
"""Module that defines the Base class."""
import json
import csv


class Base:
    """Base class that manages the id attribute for all future classes.

    This class serves as the parent class for all other classes in this
    project, providing a common id attribute and shared serialization
    methods so that subclasses don't need to reimplement them.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int): The identity of the new instance. If None, a
                unique id is generated based on the number of objects
                already created.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation, or "[]" if the list
                is None or empty.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of a list of objects.

        Args:
            list_objs (list): A list of instances who inherit of Base.
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return a list of dicts represented by a JSON string.

        Args:
            json_string (str): A JSON string representing a list of
                dictionaries.

        Returns:
            list: The list represented by json_string, or an empty
                list if json_string is None or empty.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes set from a dict.

        Args:
            **dictionary: Key/value pairs of attributes to initialize.

        Returns:
            An instance of cls with attributes set from dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from a JSON file.

        The filename is based on the class name: <Class name>.json.

        Returns:
            list: A list of instantiated objects, or an empty list if
                the file does not exist.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                list_dicts = cls.from_json_string(f.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects.

        Args:
            list_objs (list): A list of instances who inherit of Base.
        """
        filename = cls.__name__ + ".csv"
        if list_objs is None:
            list_objs = []
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            if cls.__name__ == "Rectangle":
                fields = ["id", "width", "height", "x", "y"]
            else:
                fields = ["id", "size", "x", "y"]
            for obj in list_objs:
                writer.writerow([getattr(obj, field) for field in fields])

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances loaded from a CSV file.

        The filename is based on the class name: <Class name>.csv.

        Returns:
            list: A list of instantiated objects, or an empty list if
                the file does not exist.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                reader = csv.reader(f)
                list_dicts = [
                    dict(zip(fields, map(int, row))) for row in reader
                ]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
