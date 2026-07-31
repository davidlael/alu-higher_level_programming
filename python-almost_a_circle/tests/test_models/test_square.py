#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Tests for instantiation of the Square class."""

    def test_is_rectangle(self):
        self.assertIsInstance(Square(5), Rectangle)

    def test_size_only(self):
        s = Square(5)
        self.assertEqual((s.width, s.height, s.x, s.y), (5, 5, 0, 0))

    def test_size_x(self):
        s = Square(2, 2)
        self.assertEqual((s.width, s.height, s.x, s.y), (2, 2, 2, 0))

    def test_size_x_y(self):
        s = Square(3, 1, 3)
        self.assertEqual((s.width, s.height, s.x, s.y), (3, 3, 1, 3))

    def test_no_new_attributes(self):
        s = Square(5)
        with self.assertRaises(AttributeError):
            s.width_extra

    def test_width_raises_typeerror(self):
        with self.assertRaises(TypeError):
            Square("5")


class TestSquare_area(unittest.TestCase):
    """Tests for the area method."""

    def test_area(self):
        self.assertEqual(Square(5).area(), 25)
        self.assertEqual(Square(2, 2).area(), 4)
        self.assertEqual(Square(3, 1, 3).area(), 9)


class TestSquare_display(unittest.TestCase):
    """Tests for the display method."""

    def test_display(self):
        s = Square(2)
        expected = "##\n##\n"
        with patch("sys.stdout", new=StringIO()) as fake_out:
            s.display()
            self.assertEqual(fake_out.getvalue(), expected)


class TestSquare_str(unittest.TestCase):
    """Tests for the __str__ method."""

    def test_str(self):
        s = Square(5, id=17)
        self.assertEqual(str(s), "[Square] (17) 0/0 - 5")

    def test_str_full(self):
        s = Square(3, 1, 3, 9)
        self.assertEqual(str(s), "[Square] (9) 1/3 - 3")


class TestSquare_size(unittest.TestCase):
    """Tests for the size getter/setter."""

    def test_size_getter(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        s = Square(5)
        s.size = 10
        self.assertEqual((s.width, s.height), (10, 10))

    def test_size_setter_type_error(self):
        s = Square(5)
        with self.assertRaises(TypeError) as e:
            s.size = "9"
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_size_setter_value_error(self):
        s = Square(5)
        with self.assertRaises(ValueError) as e:
            s.size = -1
        self.assertEqual(str(e.exception), "width must be > 0")


class TestSquare_update_args(unittest.TestCase):
    """Tests for the update method with *args."""

    def test_update_id(self):
        s = Square(5)
        s.update(10)
        self.assertEqual(s.id, 10)

    def test_update_all_args(self):
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")


class TestSquare_update_kwargs(unittest.TestCase):
    """Tests for the update method with **kwargs."""

    def test_update_kwargs(self):
        s = Square(5)
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 0/1 - 7")


class TestSquare_to_dictionary(unittest.TestCase):
    """Tests for the to_dictionary method."""

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 5)
        expected = {"id": 5, "size": 10, "x": 2, "y": 1}
        self.assertEqual(s.to_dictionary(), expected)

    def test_update_from_dictionary(self):
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))


if __name__ == "__main__":
    unittest.main()
