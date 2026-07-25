#!/usr/bin/python3
"""Unit tests for Square class"""
import unittest
import sys
from io import StringIO
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

    def test_id(self):
        """Test id"""
        s = Square(5, 1, 2, 3)
        self.assertEqual(s.id, 3)

    def test_auto_id(self):
        """Test auto id"""
        s1 = Square(5)
        s2 = Square(3)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)

    def test_width_equals_size(self):
        """Test width equals size"""
        s = Square(5)
        self.assertEqual(s.width, 5)

    def test_height_equals_size(self):
        """Test height equals size"""
        s = Square(5)
        self.assertEqual(s.height, 5)

    def test_size_type_string(self):
        """Test size type string"""
        with self.assertRaises(TypeError):
            Square("5")

    def test_size_type_float(self):
        """Test size type float"""
        with self.assertRaises(TypeError):
            Square(1.5)

    def test_size_type_none(self):
        """Test size type None"""
        with self.assertRaises(TypeError):
            Square(None)

    def test_size_zero(self):
        """Test size zero"""
        with self.assertRaises(ValueError):
            Square(0)

    def test_size_negative(self):
        """Test size negative"""
        with self.assertRaises(ValueError):
            Square(-5)

    def test_x_type_string(self):
        """Test x type string"""
        with self.assertRaises(TypeError):
            Square(5, "1")

    def test_x_type_float(self):
        """Test x type float"""
        with self.assertRaises(TypeError):
            Square(5, 1.5)

    def test_x_negative(self):
        """Test x negative"""
        with self.assertRaises(ValueError):
            Square(5, -1)

    def test_x_zero(self):
        """Test x zero is valid"""
        s = Square(5, 0)
        self.assertEqual(s.x, 0)

    def test_y_type_string(self):
        """Test y type string"""
        with self.assertRaises(TypeError):
            Square(5, 0, "1")

    def test_y_type_float(self):
        """Test y type float"""
        with self.assertRaises(TypeError):
            Square(5, 0, 1.5)

    def test_y_negative(self):
        """Test y negative"""
        with self.assertRaises(ValueError):
            Square(5, 0, -1)

    def test_y_zero(self):
        """Test y zero is valid"""
        s = Square(5, 0, 0)
        self.assertEqual(s.y, 0)

    def test_str(self):
        """Test str"""
        s = Square(5, 1, 2, 3)
        self.assertEqual(str(s), "[Square] (3) 1/2 - 5")

    def test_str_auto_id(self):
        """Test str auto id"""
        s = Square(5)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")

    def test_area(self):
        """Test area"""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_area_large(self):
        """Test area large"""
        s = Square(10)
        self.assertEqual(s.area(), 100)

    def test_display(self):
        """Test display"""
        s = Square(2)
        captured = StringIO()
        sys.stdout = captured
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")

    def test_display_with_xy(self):
        """Test display with x and y"""
        s = Square(2, 1, 1)
        captured = StringIO()
        sys.stdout = captured
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n ##\n ##\n")

    def test_size_getter(self):
        """Test size getter"""
        s = Square(5)
        self.assertEqual(s.size, 5)

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

    def test_size_setter_zero(self):
        """Test size setter zero"""
        s = Square(5)
        with self.assertRaises(ValueError):
            s.size = 0

    def test_update_args_id(self):
        """Test update args id"""
        s = Square(5)
        s.update(10)
        self.assertEqual(s.id, 10)

    def test_update_args_all(self):
        """Test update args all"""
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

    def test_update_kwargs_id(self):
        """Test update kwargs id"""
        s = Square(5)
        s.update(id=89)
        self.assertEqual(s.id, 89)

    def test_update_args_over_kwargs(self):
        """Test args over kwargs"""
        s = Square(5)
        s.update(10, 2, size=99)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 2)

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

    def test_to_dictionary_keys(self):
        """Test to_dictionary keys"""
        s = Square(5)
        d = s.to_dictionary()
        self.assertIn('id', d)
        self.assertIn('size', d)
        self.assertIn('x', d)
        self.assertIn('y', d)


if __name__ == '__main__':
    unittest.main()

class TestSquareErrors(unittest.TestCase):
    """Tests for Square error messages"""

    def test_size_type_message(self):
        """Test size type error message"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")

    def test_size_value_message(self):
        """Test size value error message"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_x_type_message(self):
        """Test x type error message"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, "1")

    def test_x_value_message(self):
        """Test x value error message"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1)

    def test_y_type_message(self):
        """Test y type error message"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 0, "1")

    def test_y_value_message(self):
        """Test y value error message"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(5, 0, -1)

class TestSquareDisplay(unittest.TestCase):
    """Tests for Square display method"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_display_no_offset(self):
        """Test display no offset"""
        s = Square(3)
        captured = StringIO()
        sys.stdout = captured
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "###\n###\n###\n")

    def test_display_x_only(self):
        """Test display x only"""
        s = Square(2, 2)
        captured = StringIO()
        sys.stdout = captured
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "  ##\n  ##\n")

    def test_display_y_only(self):
        """Test display y only"""
        s = Square(2, 0, 2)
        captured = StringIO()
        sys.stdout = captured
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n\n##\n##\n")

    def test_update_no_args(self):
        """Test update no args"""
        s = Square(5, 1, 2, 3)
        s.update()
        self.assertEqual(str(s), "[Square] (3) 1/2 - 5")

    def test_update_one_arg(self):
        """Test update one arg"""
        s = Square(5)
        s.update(10)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 5)

    def test_size_setter_negative(self):
        """Test size setter negative"""
        s = Square(5)
        with self.assertRaises(ValueError):
            s.size = -1

class TestSquareExtra(unittest.TestCase):
    """Extra tests for Square"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_instantiation(self):
        """Test instantiation"""
        s = Square(5)
        self.assertIsInstance(s, Square)

    def test_is_rectangle(self):
        """Test is Rectangle"""
        from models.rectangle import Rectangle
        s = Square(5)
        self.assertIsInstance(s, Rectangle)

    def test_is_base(self):
        """Test is Base"""
        from models.base import Base
        s = Square(5)
        self.assertIsInstance(s, Base)

    def test_one_arg(self):
        """Test one arg"""
        s = Square(5)
        self.assertEqual(s.id, 1)

    def test_two_args(self):
        """Test two args"""
        s = Square(5, 2)
        self.assertEqual(s.x, 2)

    def test_three_args(self):
        """Test three args"""
        s = Square(5, 2, 3)
        self.assertEqual(s.y, 3)

    def test_four_args(self):
        """Test four args"""
        s = Square(5, 2, 3, 4)
        self.assertEqual(s.id, 4)

    def test_size_private(self):
        """Test size is private"""
        with self.assertRaises(AttributeError):
            Square(5).__size

    def test_width_equals_height(self):
        """Test width equals height"""
        s = Square(5)
        self.assertEqual(s.width, s.height)

    def test_area_type(self):
        """Test area returns int"""
        s = Square(5)
        self.assertEqual(type(s.area()), int)

    def test_update_two_args(self):
        """Test update two args"""
        s = Square(5)
        s.update(10, 3)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 3)

    def test_update_three_args(self):
        """Test update three args"""
        s = Square(5)
        s.update(10, 3, 4)
        self.assertEqual(s.x, 4)

    def test_update_kwargs_size(self):
        """Test update kwargs size"""
        s = Square(5)
        s.update(size=10)
        self.assertEqual(s.size, 10)

    def test_update_kwargs_x(self):
        """Test update kwargs x"""
        s = Square(5)
        s.update(x=3)
        self.assertEqual(s.x, 3)

    def test_update_kwargs_y(self):
        """Test update kwargs y"""
        s = Square(5)
        s.update(y=3)
        self.assertEqual(s.y, 3)

    def test_to_dict_update(self):
        """Test to_dictionary then update"""
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))

    def test_str_method(self):
        """Test __str__ method exists"""
        s = Square(5)
        self.assertTrue(hasattr(s, '__str__'))

    def test_display_method(self):
        """Test display method exists"""
        s = Square(5)
        self.assertTrue(hasattr(s, 'display'))

    def test_area_method(self):
        """Test area method exists"""
        s = Square(5)
        self.assertTrue(hasattr(s, 'area'))

    def test_size_type_tuple(self):
        """Test size type tuple"""
        with self.assertRaises(TypeError):
            Square((1,))

    def test_size_type_dict(self):
        """Test size type dict"""
        with self.assertRaises(TypeError):
            Square({})

    def test_x_type_none(self):
        """Test x type None"""
        with self.assertRaises(TypeError):
            Square(5, None)

    def test_y_type_none(self):
        """Test y type None"""
        with self.assertRaises(TypeError):
            Square(5, 0, None)
