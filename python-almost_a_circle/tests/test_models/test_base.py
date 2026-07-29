#!/usr/bin/python3
"""Unit tests for the Base class."""
import os
import unittest
from base import Base
from rectangle import Rectangle
from square import Square


class TestBase(unittest.TestCase):
    """Tests for the Base class."""

    def test_id_public(self):
        """Test that a given id is stored as-is."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_none_generates_unique(self):
        """Test that id auto-increments when None is passed."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_to_json_string_empty(self):
        """Test to_json_string with an empty or None list."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list(self):
        """Test to_json_string with a list of dictionaries."""
        list_dicts = [{"id": 1}, {"id": 2}]
        result = Base.to_json_string(list_dicts)
        self.assertIsInstance(result, str)

    def test_from_json_string_empty(self):
        """Test from_json_string with an empty or None string."""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_roundtrip(self):
        """Test that to_json_string and from_json_string round-trip."""
        list_dicts = [{"id": 1, "width": 2}]
        json_str = Base.to_json_string(list_dicts)
        self.assertEqual(Base.from_json_string(json_str), list_dicts)

    def test_save_and_load_to_file(self):
        """Test save_to_file and load_from_file for Rectangle."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 2)
        self.assertEqual(rectangles[0].to_dictionary(), r1.to_dictionary())
        os.remove("Rectangle.json")

    def test_load_from_file_no_file(self):
        """Test load_from_file returns [] when no file exists."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_save_to_file_none(self):
        """Test save_to_file with None writes an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Rectangle.json")

    def test_save_and_load_csv_rectangle(self):
        """Test save_to_file_csv and load_from_file_csv for Rectangle."""
        r1 = Rectangle(3, 5, 1, 1, 99)
        Rectangle.save_to_file_csv([r1])
        rectangles = Rectangle.load_from_file_csv()
        self.assertEqual(rectangles[0].to_dictionary(), r1.to_dictionary())
        os.remove("Rectangle.csv")

    def test_save_and_load_csv_square(self):
        """Test save_to_file_csv and load_from_file_csv for Square."""
        s1 = Square(5, 1, 1, 99)
        Square.save_to_file_csv([s1])
        squares = Square.load_from_file_csv()
        self.assertEqual(squares[0].to_dictionary(), s1.to_dictionary())
        os.remove("Square.csv")


if __name__ == "__main__":
    unittest.main()
