#!/usr/bin/python3
"""Contains Testcases for Review Class"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Testcases for Review class"""
    def test_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()
