#!/usr/bin/python3
"""Contains Testcases for Amenity Class"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Testcases for Amenity class"""
    def test_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
