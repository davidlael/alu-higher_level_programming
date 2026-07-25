#!/usr/bin/python3
"""Module for Base class"""
import json
import csv
import os


class Base:
    """Base class for managing id attribute"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        list_dicts = [o.to_dictionary() for o in list_objs]
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns list represented by json_string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls == Rectangle:
            dummy = Rectangle(1, 1)
        else:
            dummy = Square(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                list_dicts = cls.from_json_string(f.read())
            return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs to CSV file"""
        filename = cls.__name__ + ".csv"
        if list_objs is None:
            list_objs = []
        with open(filename, "w", newline='') as f:
            writer = csv.writer(f)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    row = [obj.id, obj.width, obj.height, obj.x, obj.y]
                else:
                    row = [obj.id, obj.size, obj.x, obj.y]
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV file to list of instances"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline='') as f:
                reader = csv.reader(f)
                instances = []
                for row in reader:
                    row = [int(x) for x in row]
                    if cls.__name__ == "Rectangle":
                        d = {
                            "id": row[0],
                            "width": row[1],
                            "height": row[2],
                            "x": row[3],
                            "y": row[4]
                        }
                    else:
                        d = {
                            "id": row[0],
                            "size": row[1],
                            "x": row[2],
                            "y": row[3]
                        }
                    instances.append(cls.create(**d))
                return instances
        except FileNotFoundError:
            return []
