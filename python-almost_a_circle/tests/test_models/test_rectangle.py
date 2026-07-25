#!/usr/bin/python3
"""Unit tests for Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle class"""

    def setUp(self):
        """Reset __nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_basic(self):
        """Test basic Rectangle creation"""
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)

    def test_width_type(self):
        """Test width type validation"""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_width_value(self):
        """Test width value validation"""
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)

    def test_height_type(self):
        """Test height type validation"""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_height_value(self):
        """Test height value validation"""
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_x_type(self):
        """Test x type validation"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, {})

    def test_x_value(self):
        """Test x value validation"""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1)

    def test_y_type(self):
        """Test y type validation"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, "1")

    def test_y_value(self):
        """Test y value validation"""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 0, -1)

    def test_area(self):
        """Test area method"""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        """Test __str__ method"""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        """Test update with args"""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)

    def test_update_kwargs(self):
        """Test update with kwargs"""
        r = Rectangle(10, 10)
        r.update(height=1)
        self.assertEqual(r.height, 1)

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        r = Rectangle(10, 2, 1, 9)
        d = r.to_dictionary()
        self.assertIn('width', d)
        self.assertIn('height', d)


if __name__ == '__main__':
    unittest.main()
