#!/usr/bin/python3
"""Unit tests for Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_basic(self):
        """Test basic creation"""
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)

    def test_default_x_y(self):
        """Test default x and y"""
        r = Rectangle(10, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_id(self):
        """Test id"""
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)

    def test_width_type(self):
        """Test width type"""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)

    def test_width_zero(self):
        """Test width zero"""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_width_negative(self):
        """Test width negative"""
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)

    def test_height_type(self):
        """Test height type"""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_height_zero(self):
        """Test height zero"""
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_height_negative(self):
        """Test height negative"""
        with self.assertRaises(ValueError):
            Rectangle(10, -2)

    def test_x_type(self):
        """Test x type"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, {})

    def test_x_negative(self):
        """Test x negative"""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1)

    def test_y_type(self):
        """Test y type"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, "1")

    def test_y_negative(self):
        """Test y negative"""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 0, -1)

    def test_area(self):
        """Test area"""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_area_large(self):
        """Test area large"""
        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r.area(), 56)

    def test_str(self):
        """Test str"""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        """Test update args"""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_kwargs(self):
        """Test update kwargs"""
        r = Rectangle(10, 10)
        r.update(height=1, width=2)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.width, 2)

    def test_to_dictionary(self):
        """Test to_dictionary"""
        r = Rectangle(10, 2, 1, 9)
        d = r.to_dictionary()
        self.assertEqual(d['width'], 10)
        self.assertEqual(d['height'], 2)
        self.assertEqual(d['x'], 1)
        self.assertEqual(d['y'], 9)

    def test_to_dictionary_type(self):
        """Test to_dictionary type"""
        r = Rectangle(10, 2)
        self.assertEqual(type(r.to_dictionary()), dict)


if __name__ == '__main__':
    unittest.main()
