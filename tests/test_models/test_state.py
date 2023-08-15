#!/usr/bin/python3
"""Contains Testcases for State Class"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Testcases for state class"""
    def test_attributes(self):
        state = State()
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
