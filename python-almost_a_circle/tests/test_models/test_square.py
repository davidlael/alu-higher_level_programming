#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
from square import Square


class TestSquare(unittest.TestCase):
    """Tests for the Square class."""

    def test_normal_creation(self):
        """Test creating a Square with all attributes."""
        s = Square(5, 1, 1, 12)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 1)
        self.assertEqual(s.id, 12)

    def test_size_property_get(self):
        """Test that size returns the same as width and height."""
        s = Square(7)
        self.assertEqual(s.size, 7)

    def test_size_property_set(self):
        """Test that setting size updates both width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_str(self):
        """Test the string representation."""
        s = Square(4, 2, 1, 5)
        self.assertEqual(str(s), "[Square] (5) 2/1 - 4")

    def test_update_args(self):
        """Test update with positional arguments."""
        s = Square(10, 10, 10, 1)
        s.update(1, 2, 3, 4)
        self.assertEqual((s.id, s.size, s.x, s.y), (1, 2, 3, 4))

    def test_update_kwargs(self):
        """Test update with keyword arguments."""
        s = Square(10, 10, 10, 1)
        s.update(size=2, x=3)
        self.assertEqual((s.size, s.x), (2, 3))

    def test_to_dictionary(self):
        """Test that to_dictionary returns the correct dict."""
        s = Square(5, 1, 1, 12)
        expected = {"id": 12, "size": 5, "x": 1, "y": 1}
        self.assertEqual(s.to_dictionary(), expected)

    def test_width_value_error(self):
        """Test that a size <= 0 raises ValueError."""
        with self.assertRaises(ValueError):
            Square(0)


if __name__ == "__main__":
    unittest.main()
