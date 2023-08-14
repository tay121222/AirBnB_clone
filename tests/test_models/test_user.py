#!/usr/bin/python3
"""Contains Testcases for User Class"""

import unittest
from models.user import User
from datetime import datetime
import json
import os

class TestUser(unittest.TestCase):
    """Testcase for User Class"""
    
    def test_instance_creation(self):
        user = User()
        self.assertIsInstance(user, User)
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_attributes_initialization(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_string_representation(self):
        user = User()
        self.assertEqual(str(user), "[User] ({}) {}".format(user.id, user.__dict__))

    def test_save_method(self):
        user = User()
        old_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(old_updated_at, user.updated_at)
