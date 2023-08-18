#!/usr/bin/python3
"""Unittests for base_model"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """Unittest cases for base_class I can think of"""

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        try:
            FileStorage._FileStorage__objects = {}
            if os.path.isfile(FileStorage._FileStorage__file_path):
                os.remove(self.storage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_all_empty(self):
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 0)

    def test_new(self):
        obj = BaseModel()
        self.storage.new(obj)
        all_objects = self.storage.all()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, all_objects)

    def test_save_reload(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        all_objects = new_storage.all()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, all_objects)

    def test_save_reload_multiple_objects(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        all_objects = new_storage.all()
        key1 = "{}.{}".format(obj1.__class__.__name__, obj1.id)
        key2 = "{}.{}".format(obj2.__class__.__name__, obj2.id)
        self.assertIn(key1, all_objects)
        self.assertIn(key2, all_objects)

    def test_reload_no_file(self):
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertEqual(len(all_objects), 0)

    def test_file_path_exists(self):
        fs = FileStorage()
        self.assertTrue(hasattr(fs, '_FileStorage__file_path'))
        self.assertIsInstance(fs._FileStorage__file_path, str)

    def test_file_path_attribute(self):
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_objects_attribute(self):
        self.assertEqual(self.storage._FileStorage__objects, {})


if __name__ == '__main__':
    unittest.main()
