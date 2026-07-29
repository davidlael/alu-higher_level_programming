#!/usr/bin/python3
"""Defines the Square class inheriting from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a Square shape."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance.

        Args:
            size (int): Size of the square side.
            x (int): Horizontal position.
            y (int): Vertical position.
            id (int): Identification.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get size of square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set size of square."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return string representation of Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Assign arguments to attributes via args or kwargs."""
        attrs = ["id", "size", "x", "y"]
        if args and len(args) > 0:
            for idx, arg in enumerate(args):
                if idx < len(attrs):
                    setattr(self, attrs[idx], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
