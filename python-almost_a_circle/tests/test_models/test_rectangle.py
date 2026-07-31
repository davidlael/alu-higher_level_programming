#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Tests for instantiation of the Rectangle class."""

    def test_is_base(self):
        self.assertIsInstance(Rectangle(1, 1), Base)

    def test_width_height(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_all_args(self):
        r = Rectangle(10, 2, 1, 3, 12)
        expected = (10, 2, 1, 3, 12)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id), expected)

    def test_id_increments(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, r1.id + 1)

    def test_width_type_error(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, "2")
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_width_not_int(self):
        with self.assertRaises(TypeError) as e:
            Rectangle("10", 2)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_width_negative(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(-10, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_width_zero(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(0, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_height_negative(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(10, -2)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_x_not_int(self):
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 2, {})
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_x_negative(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(10, 2, -1)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_y_negative(self):
        with self.assertRaises(ValueError) as e:
            Rectangle(10, 2, 3, -1)
        self.assertEqual(str(e.exception), "y must be >= 0")


class TestRectangle_setters(unittest.TestCase):
    """Tests for the setters of Rectangle attributes."""

    def test_width_setter_raises(self):
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.width = -10

    def test_height_setter_raises(self):
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r.height = "10"


class TestRectangle_area(unittest.TestCase):
    """Tests for the area method."""

    def test_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_area_too_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 2).area(1)


class TestRectangle_display(unittest.TestCase):
    """Tests for the display method."""

    def test_display_basic(self):
        r = Rectangle(2, 2)
        expected = "##\n##\n"
        with patch("sys.stdout", new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), expected)

    def test_display_with_x_y(self):
        r = Rectangle(2, 3, 2, 2)
        expected = "\n\n  ##\n  ##\n  ##\n"
        with patch("sys.stdout", new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), expected)


class TestRectangle_str(unittest.TestCase):
    """Tests for the __str__ method."""

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_str_default(self):
        r = Rectangle(5, 5, 1, id=42)
        self.assertEqual(str(r), "[Rectangle] (42) 1/0 - 5/5")


class TestRectangle_update_args(unittest.TestCase):
    """Tests for the update method with *args."""

    def test_update_no_args(self):
        r = Rectangle(10, 10, 10, 10, id=7)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (7) 10/10 - 10/10")

    def test_update_id(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_all_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")


class TestRectangle_update_kwargs(unittest.TestCase):
    """Tests for the update method with **kwargs."""

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(x=1, height=2, y=3, width=4, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 1/3 - 4/2")

    def test_update_kwargs_partial(self):
        r = Rectangle(10, 10, 10, 10, id=3)
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (3) 10/10 - 10/1")


class TestRectangle_to_dictionary(unittest.TestCase):
    """Tests for the to_dictionary method."""

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 2)
        expected = {"id": 2, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(r.to_dictionary(), expected)

    def test_to_dictionary_is_independent(self):
        r = Rectangle(10, 2, 1, 9, 2)
        d = r.to_dictionary()
        d["width"] = 100
        self.assertEqual(r.width, 10)

    def test_update_from_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))


if __name__ == "__main__":
    unittest.main()
