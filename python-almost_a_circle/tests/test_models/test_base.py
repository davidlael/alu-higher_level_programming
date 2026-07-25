#!/usr/bin/python3
"""Unit tests for Base class"""
import unittest
from models.base import Base


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

    def test_to_json_string_empty(self):
        """Test to_json_string empty"""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_none(self):
        """Test to_json_string None"""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_type(self):
        """Test to_json_string returns str"""
        self.assertEqual(type(Base.to_json_string([{"id": 1}])), str)

    def test_from_json_string_empty(self):
        """Test from_json_string empty"""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_none(self):
        """Test from_json_string None"""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string(self):
        """Test from_json_string"""
        self.assertEqual(Base.from_json_string('[{"id": 1}]'), [{"id": 1}])


if __name__ == '__main__':
    unittest.main()
