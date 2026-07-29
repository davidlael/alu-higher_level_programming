#!/usr/bin/python3
"""Unittests for testing the Square class and its methods."""
import os
import unittest
from models.square import Square


class TestSquareSaveToFile(unittest.TestCase):
    """Unittests for testing save_to_file method of Square class."""

    def tearDown(self):
        """Clean up created files after each test."""
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_save_to_file_none(self):
        """Test save_to_file with None as input."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        """Test save_to_file with an empty list as input."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")


if __name__ == "__main__":
    unittest.main()
