#!/usr/bin/python3
"""Module that defines the Square class."""
from rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle.

    A square is represented as a rectangle whose width and height
    are always equal.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance.

        Args:
            size (int): The size (width and height) of the square.
            x (int): The x coordinate of the square.
            y (int): The y coordinate of the square.
            id (int): The identity of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """int: The size of the square (mirrors width and height)."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update attributes via *args or **kwargs.

        Args:
            *args: New attribute values in order: id, size, x, y.
            **kwargs: New attribute values by key/value pairs.
        """
        if args and len(args) > 0:
            attrs = ["id", "size", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
