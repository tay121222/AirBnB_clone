#!/usr/bin/python3
"""Unittests for base_model"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
import os


class TestBaseModel(unittest.TestCase):
    """Unittest cases for base_class I can think of"""

    def setUp(self):
        self.storage = FileStorage()
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_attributes(self):
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_create_instance(self):
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)

    def test_id_generation(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_created_at(self):
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)

    def test_updated_at(self):
        obj = BaseModel()
        self.assertIsInstance(obj.updated_at, datetime)

    def test_to_dict(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertTrue(isinstance(obj_dict, dict))
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertTrue('id' in obj_dict)
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)

    def test_str_representation(self):
        obj = BaseModel()
        obj_str = str(obj)
        self.assertIn('[BaseModel]', obj_str)
        self.assertIn(obj.id, obj_str)
        self.assertIn(str(obj.__dict__), obj_str)

    def test_init(self):
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertEqual(model.created_at, model.updated_at)

    def test_str(self):
        model = BaseModel()
        model_str = str(model)
        self.assertTrue(model.__class__.__name__ in model_str)
        self.assertTrue(model.id in model_str)

    def test_save(self):
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_init_with_kwargs(self):
        kwargs = {
                'id': 'test_id',
                'created_at': '2023-08-01T12:00:00.000000',
                'updated_at': '2023-08-02T12:00:00.000000',
                'name': 'test_name'
                }
        model = BaseModel(**kwargs)
        self.assertEqual(model.id, kwargs['id'])
        self.assertEqual(model.created_at, datetime.strptime(
            kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            )
        self.assertEqual(
                model.updated_at, datetime.strptime
                (kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            )
        self.assertTrue(hasattr(model, 'name'))

    def test_kwargs_constructor(self):
        instance = BaseModel(name="Test", value=123)
        self.assertEqual(instance.name, "Test")
        self.assertEqual(instance.value, 123)

    def test_invalid_datetime_format(self):
        instance_dict = {
                'id': '12345',
                'created_at': '2023-08-10T12:30:45',
                'updated_at': '2023-08-10T12:30:45.123456'
                }
        with self.assertRaises(ValueError):
            BaseModel(**instance_dict)

    def test_access_class_attribute(self):
        instance = BaseModel()
        self.assertEqual(instance.__class__.__name__, 'BaseModel')

    def test_unique_ids(self):
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_update_attributes(self):
        instance = BaseModel()
        original_updated_at = instance.updated_at
        instance.name = "Updated Name"
        instance.value = 456
        instance.save()
        self.assertNotEqual(original_updated_at, instance.updated_at)

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

if __name__ == '__main__':
    unittest.main()
