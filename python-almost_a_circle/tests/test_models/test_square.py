#!/usr/bin/python3
"""Unit tests for Square class"""
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for Square class"""

    def setUp(self):
        """Reset __nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_basic(self):
        """Test basic Square creation"""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_type(self):
        """Test size type validation"""
        with self.assertRaises(TypeError):
            Square("5")

    def test_size_value(self):
        """Test size value validation"""
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        """Test __str__ method"""
        s = Square(5, 1, 2, 3)
        self.assertEqual(str(s), "[Square] (3) 1/2 - 5")

    def test_area(self):
        """Test area method"""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_update_args(self):
        """Test update with args"""
        s = Square(5)
        s.update(10, 2, 3, 4)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 2)

    def test_update_kwargs(self):
        """Test update with kwargs"""
        s = Square(5)
        s.update(size=7)
        self.assertEqual(s.size, 7)

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        s = Square(10, 2, 1)
        d = s.to_dictionary()
        self.assertIn('size', d)
        self.assertIn('id', d)

    def test_size_setter(self):
        """Test size setter"""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)


if __name__ == '__main__':
    unittest.main()
