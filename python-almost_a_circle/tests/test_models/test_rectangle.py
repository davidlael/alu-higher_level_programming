#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
from rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class."""

    def test_normal_creation(self):
        """Test creating a Rectangle with all attributes."""
        r = Rectangle(10, 2, 1, 1, 12)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 12)

    def test_default_x_y(self):
        """Test that x and y default to 0."""
        r = Rectangle(3, 4)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_width_type_error(self):
        """Test that a non-integer width raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)

    def test_height_type_error(self):
        """Test that a non-integer height raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_width_value_error(self):
        """Test that a width <= 0 raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_x_negative(self):
        """Test that a negative x raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(2, 2, -1)

    def test_y_negative(self):
        """Test that a negative y raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(2, 2, 0, -1)

    def test_area(self):
        """Test the area calculation."""
        r = Rectangle(3, 5)
        self.assertEqual(r.area(), 15)

    def test_str(self):
        """Test the string representation."""
        r = Rectangle(4, 6, 2, 1, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 2/1 - 4/6")

    def test_update_args(self):
        """Test update with positional arguments."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(1, 2, 3, 4, 5)
        self.assertEqual(
            (r.id, r.width, r.height, r.x, r.y), (1, 2, 3, 4, 5))

    def test_update_kwargs(self):
        """Test update with keyword arguments."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(width=1, height=2)
        self.assertEqual((r.width, r.height), (1, 2))

    def test_to_dictionary(self):
        """Test that to_dictionary returns the correct dict."""
        r = Rectangle(10, 2, 1, 1, 12)
        expected = {"id": 12, "width": 10, "height": 2, "x": 1, "y": 1}
        self.assertEqual(r.to_dictionary(), expected)


if __name__ == "__main__":
    unittest.main()
