#!/usr/bin/python3
"""Unittests for testing the Rectangle class and its methods."""
import os
import unittest
from models.rectangle import Rectangle


class TestRectangleSaveToFile(unittest.TestCase):
    """Unittests for testing save_to_file method of Rectangle class."""

    def tearDown(self):
        """Clean up created files after each test."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass

    def test_save_to_file_none(self):
        """Test save_to_file with None as input."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        """Test save_to_file with an empty list as input."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")


if __name__ == "__main__":
    unittest.main()
