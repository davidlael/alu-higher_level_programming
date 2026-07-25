#!/usr/bin/python3
"""Unit tests for Rectangle class"""
import unittest
import sys
from io import StringIO
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

    def test_auto_id(self):
        """Test auto id"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(5, 3)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)

    def test_width_getter(self):
        """Test width getter"""
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)

    def test_width_setter(self):
        """Test width setter"""
        r = Rectangle(10, 2)
        r.width = 5
        self.assertEqual(r.width, 5)

    def test_height_getter(self):
        """Test height getter"""
        r = Rectangle(10, 2)
        self.assertEqual(r.height, 2)

    def test_height_setter(self):
        """Test height setter"""
        r = Rectangle(10, 2)
        r.height = 5
        self.assertEqual(r.height, 5)

    def test_x_getter(self):
        """Test x getter"""
        r = Rectangle(10, 2, 3)
        self.assertEqual(r.x, 3)

    def test_x_setter(self):
        """Test x setter"""
        r = Rectangle(10, 2)
        r.x = 5
        self.assertEqual(r.x, 5)

    def test_y_getter(self):
        """Test y getter"""
        r = Rectangle(10, 2, 0, 4)
        self.assertEqual(r.y, 4)

    def test_y_setter(self):
        """Test y setter"""
        r = Rectangle(10, 2)
        r.y = 5
        self.assertEqual(r.y, 5)

    def test_width_type_string(self):
        """Test width type string"""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)

    def test_width_type_float(self):
        """Test width type float"""
        with self.assertRaises(TypeError):
            Rectangle(1.5, 2)

    def test_width_type_none(self):
        """Test width type None"""
        with self.assertRaises(TypeError):
            Rectangle(None, 2)

    def test_width_type_list(self):
        """Test width type list"""
        with self.assertRaises(TypeError):
            Rectangle([1], 2)

    def test_width_zero(self):
        """Test width zero"""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_width_negative(self):
        """Test width negative"""
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)

    def test_height_type_string(self):
        """Test height type string"""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_height_type_float(self):
        """Test height type float"""
        with self.assertRaises(TypeError):
            Rectangle(10, 1.5)

    def test_height_type_none(self):
        """Test height type None"""
        with self.assertRaises(TypeError):
            Rectangle(10, None)

    def test_height_zero(self):
        """Test height zero"""
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_height_negative(self):
        """Test height negative"""
        with self.assertRaises(ValueError):
            Rectangle(10, -2)

    def test_x_type_string(self):
        """Test x type string"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "1")

    def test_x_type_float(self):
        """Test x type float"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 1.5)

    def test_x_type_dict(self):
        """Test x type dict"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, {})

    def test_x_negative(self):
        """Test x negative"""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1)

    def test_x_zero(self):
        """Test x zero is valid"""
        r = Rectangle(10, 2, 0)
        self.assertEqual(r.x, 0)

    def test_y_type_string(self):
        """Test y type string"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, "1")

    def test_y_type_float(self):
        """Test y type float"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, 1.5)

    def test_y_negative(self):
        """Test y negative"""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 0, -1)

    def test_y_zero(self):
        """Test y zero is valid"""
        r = Rectangle(10, 2, 0, 0)
        self.assertEqual(r.y, 0)

    def test_area(self):
        """Test area"""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_area_large(self):
        """Test area large"""
        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r.area(), 56)

    def test_area_wide(self):
        """Test area wide"""
        r = Rectangle(2, 10)
        self.assertEqual(r.area(), 20)

    def test_display(self):
        """Test display"""
        r = Rectangle(2, 2)
        captured = StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")

    def test_display_with_xy(self):
        """Test display with x and y"""
        r = Rectangle(2, 2, 1, 1)
        captured = StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n ##\n ##\n")

    def test_str(self):
        """Test str"""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_str_auto_id(self):
        """Test str auto id"""
        r = Rectangle(5, 5, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 1/0 - 5/5")

    def test_update_args_id(self):
        """Test update args id"""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_args_all(self):
        """Test update args all"""
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

    def test_update_kwargs_id(self):
        """Test update kwargs id"""
        r = Rectangle(10, 10)
        r.update(id=89)
        self.assertEqual(r.id, 89)

    def test_update_args_over_kwargs(self):
        """Test args takes priority over kwargs"""
        r = Rectangle(10, 10)
        r.update(89, 2, height=5)
        self.assertEqual(r.id, 89)
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

    def test_to_dictionary_keys(self):
        """Test to_dictionary has all keys"""
        r = Rectangle(10, 2, 1, 9)
        d = r.to_dictionary()
        self.assertIn('id', d)
        self.assertIn('width', d)
        self.assertIn('height', d)
        self.assertIn('x', d)
        self.assertIn('y', d)


if __name__ == '__main__':
    unittest.main()
