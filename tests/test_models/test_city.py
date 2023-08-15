#!/usr/bin/python3
"""Contains Testcases for City Class"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Testcases for City Class"""
    def test_attributes(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()
