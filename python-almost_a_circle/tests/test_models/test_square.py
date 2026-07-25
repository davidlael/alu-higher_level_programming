#!/usr/bin/python3
"""Unit tests for Square class"""
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for Square class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_basic(self):
        """Test basic creation"""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_default_x_y(self):
        """Test default x y"""
        s = Square(5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_size_type(self):
        """Test size type"""
        with self.assertRaises(TypeError):
            Square("5")

    def test_size_zero(self):
        """Test size zero"""
        with self.assertRaises(ValueError):
            Square(0)

    def test_size_negative(self):
        """Test size negative"""
        with self.assertRaises(ValueError):
            Square(-5)

    def test_x_type(self):
        """Test x type"""
        with self.assertRaises(TypeError):
            Square(5, "1")

    def test_x_negative(self):
        """Test x negative"""
        with self.assertRaises(ValueError):
            Square(5, -1)

    def test_y_type(self):
        """Test y type"""
        with self.assertRaises(TypeError):
            Square(5, 0, "1")

    def test_y_negative(self):
        """Test y negative"""
        with self.assertRaises(ValueError):
            Square(5, 0, -1)

    def test_str(self):
        """Test str"""
        s = Square(5, 1, 2, 3)
        self.assertEqual(str(s), "[Square] (3) 1/2 - 5")

    def test_area(self):
        """Test area"""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_size_setter(self):
        """Test size setter"""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_setter_type(self):
        """Test size setter type"""
        s = Square(5)
        with self.assertRaises(TypeError):
            s.size = "9"

    def test_update_args(self):
        """Test update args"""
        s = Square(5)
        s.update(10, 2, 3, 4)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        """Test update kwargs"""
        s = Square(5)
        s.update(size=7, y=1)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.y, 1)

    def test_to_dictionary(self):
        """Test to_dictionary"""
        s = Square(10, 2, 1)
        d = s.to_dictionary()
        self.assertEqual(d['size'], 10)
        self.assertEqual(d['x'], 2)
        self.assertEqual(d['y'], 1)

    def test_to_dictionary_type(self):
        """Test to_dictionary type"""
        s = Square(5)
        self.assertEqual(type(s.to_dictionary()), dict)


if __name__ == '__main__':
    unittest.main()
