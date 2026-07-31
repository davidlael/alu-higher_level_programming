#!/usr/bin/python3
"""Unit tests for the Base class."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Tests for instantiation of the Base class."""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_public(self):
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_id_none(self):
        b = Base(None)
        self.assertIsInstance(b.id, int)

    def test_id_str(self):
        b = Base("hello")
        self.assertEqual(b.id, "hello")

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase_to_json_string(unittest.TestCase):
    """Tests for Base.to_json_string."""

    def test_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_list_of_dicts(self):
        list_dicts = [{"id": 1}, {"id": 2}]
        result = Base.to_json_string(list_dicts)
        self.assertIsInstance(result, str)
        self.assertEqual(eval(result), list_dicts)

    def test_return_type(self):
        self.assertIsInstance(Base.to_json_string([]), str)

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], [])


class TestBase_from_json_string(unittest.TestCase):
    """Tests for Base.from_json_string."""

    def test_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string(self):
        self.assertEqual(Base.from_json_string(""), [])

    def test_valid_json(self):
        list_dicts = [{"id": 1}, {"id": 2}]
        json_string = Base.to_json_string(list_dicts)
        self.assertEqual(Base.from_json_string(json_string), list_dicts)

    def test_return_type(self):
        self.assertIsInstance(Base.from_json_string("[]"), list)

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string("[]", "[]")


class TestBase_save_to_file(unittest.TestCase):
    """Tests for Base.save_to_file."""

    def tearDown(self):
        for filename in ("Rectangle.json", "Square.json"):
            if os.path.exists(filename):
                os.remove(filename)

    def test_save_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, id=100)
        r2 = Rectangle(2, 4, id=101)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertIn('"id": 100', content)
        self.assertIn('"id": 101', content)

    def test_save_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_overwrite(self):
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        r2 = Rectangle(1, 1)
        Rectangle.save_to_file([r2])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertNotIn('"width": 10', content)


class TestBase_create(unittest.TestCase):
    """Tests for Base.create."""

    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)
        self.assertEqual(str(r1), str(r2))

    def test_create_square(self):
        s1 = Square(3, 1, 2, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)
        self.assertEqual(str(s1), str(s2))


class TestBase_load_from_file(unittest.TestCase):
    """Tests for Base.load_from_file."""

    def tearDown(self):
        for filename in ("Rectangle.json", "Square.json"):
            if os.path.exists(filename):
                os.remove(filename)

    def test_no_file(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        list_output = Rectangle.load_from_file()
        self.assertEqual(len(list_output), 2)
        for rect in list_output:
            self.assertIsInstance(rect, Rectangle)

    def test_load_squares(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        list_output = Square.load_from_file()
        self.assertEqual(len(list_output), 2)
        for sq in list_output:
            self.assertIsInstance(sq, Square)


class TestBase_csv(unittest.TestCase):
    """Tests for Base.save_to_file_csv and Base.load_from_file_csv."""

    def tearDown(self):
        for filename in ("Rectangle.csv", "Square.csv"):
            if os.path.exists(filename):
                os.remove(filename)

    def test_no_file(self):
        if os.path.exists("Rectangle.csv"):
            os.remove("Rectangle.csv")
        self.assertEqual(Rectangle.load_from_file_csv(), [])

    def test_save_load_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        list_output = Rectangle.load_from_file_csv()
        self.assertEqual(len(list_output), 2)
        self.assertEqual(str(list_output[0]), str(r1))
        self.assertEqual(str(list_output[1]), str(r2))

    def test_save_load_squares(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file_csv([s1, s2])
        list_output = Square.load_from_file_csv()
        self.assertEqual(len(list_output), 2)
        self.assertEqual(str(list_output[0]), str(s1))
        self.assertEqual(str(list_output[1]), str(s2))


if __name__ == "__main__":
    unittest.main()
