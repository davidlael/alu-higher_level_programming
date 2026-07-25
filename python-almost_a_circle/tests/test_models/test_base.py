#!/usr/bin/python3
"""Unit tests for Base class"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for Base class"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id_auto(self):
        """Test auto id"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id_auto_multiple(self):
        """Test multiple auto ids"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_id_given(self):
        """Test manual id"""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_zero(self):
        """Test id zero"""
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_id_negative(self):
        """Test negative id"""
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_id_none(self):
        """Test None id"""
        b = Base(None)
        self.assertEqual(b.id, 1)

    def test_id_string(self):
        """Test string id"""
        b = Base("hello")
        self.assertEqual(b.id, "hello")

    def test_id_float(self):
        """Test float id"""
        b = Base(1.5)
        self.assertEqual(b.id, 1.5)

    def test_to_json_string_empty(self):
        """Test to_json_string empty"""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_none(self):
        """Test to_json_string None"""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_type(self):
        """Test to_json_string returns str"""
        self.assertEqual(type(Base.to_json_string([{"id": 1}])), str)

    def test_to_json_string_data(self):
        """Test to_json_string with data"""
        import json
        d = [{"id": 1, "width": 10}]
        result = Base.to_json_string(d)
        self.assertEqual(json.loads(result), d)

    def test_from_json_string_empty(self):
        """Test from_json_string empty"""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_none(self):
        """Test from_json_string None"""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string(self):
        """Test from_json_string"""
        self.assertEqual(
            Base.from_json_string('[{"id": 1}]'), [{"id": 1}])

    def test_from_json_string_type(self):
        """Test from_json_string returns list"""
        self.assertEqual(
            type(Base.from_json_string('[{"id": 1}]')), list)

    def test_save_to_file_rectangle(self):
        """Test save_to_file with Rectangle"""
        r = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_save_to_file_none(self):
        """Test save_to_file with None"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        """Test save_to_file with empty list"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_load_from_file_rectangle(self):
        """Test load_from_file with Rectangle"""
        r = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r])
        result = Rectangle.load_from_file()
        self.assertEqual(len(result), 1)
        self.assertEqual(str(result[0]), str(r))

    def test_load_from_file_no_file(self):
        """Test load_from_file when no file"""
        if os.path.exists("NoFile.json"):
            os.remove("NoFile.json")
        result = Base.load_from_file()
        self.assertEqual(result, [])

    def test_create_rectangle(self):
        """Test create with Rectangle"""
        r = Rectangle(3, 5, 1)
        r_dict = r.to_dictionary()
        r2 = Rectangle.create(**r_dict)
        self.assertEqual(str(r), str(r2))

    def test_create_square(self):
        """Test create with Square"""
        s = Square(5, 2, 1)
        s_dict = s.to_dictionary()
        s2 = Square.create(**s_dict)
        self.assertEqual(str(s), str(s2))


if __name__ == '__main__':
    unittest.main()

class TestBaseSaveLoad(unittest.TestCase):
    """Tests for save and load"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_save_to_file_square(self):
        """Test save_to_file with Square"""
        s = Square(5)
        Square.save_to_file([s])
        self.assertTrue(os.path.exists("Square.json"))

    def test_load_from_file_square(self):
        """Test load_from_file with Square"""
        s = Square(5, 2, 1)
        Square.save_to_file([s])
        result = Square.load_from_file()
        self.assertEqual(len(result), 1)
        self.assertEqual(str(result[0]), str(s))

    def test_load_from_file_multiple(self):
        """Test load_from_file multiple"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        result = Rectangle.load_from_file()
        self.assertEqual(len(result), 2)

    def test_save_to_file_overwrites(self):
        """Test save_to_file overwrites"""
        r1 = Rectangle(10, 7)
        Rectangle.save_to_file([r1])
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r2])
        result = Rectangle.load_from_file()
        self.assertEqual(len(result), 1)
