#!/usr/bin/python3
"""Defines unittests for console.py"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os
from models.engine.file_storage import FileStorage


class TestHBNBCommand(unittest.TestCase):
    """Unit Testcases for console.py"""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        storage.clear_all()

    def test_emptyline(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.emptyline()
            self.assertEqual(output.getvalue(), "")

    def test_do_quit(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(self.console.do_quit(""))
            self.assertEqual(output.getvalue(), "")

    def test_do_EOF(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(self.console.do_EOF(""))
            self.assertEqual(output.getvalue(), "")

    def test_do_create(self):
        with patch("sys.stdout", new=StringIO()) as output:
            with patch('models.engine.file_storage.FileStorage.save') as mock_save:
                self.console.do_create("BaseModel")
                self.assertTrue(mock_save.called)
                self.assertEqual(output.getvalue().startswith(''), True)

        with patch("sys.stdout", new=StringIO()) as output:
            with patch('models.engine.file_storage.FileStorage.save') as mock_save:
                self.console.do_create("InvalidModel")
                self.assertFalse(mock_save.called)
                self.assertEqual(output.getvalue().strip(), "** class doesn't exist **")

    def test_show_base_model(self):
        with patch("sys.stdout", new=StringIO()) as output:
            obj = BaseModel()
            self.console.do_show("BaseModel " + obj.id)
            self.assertTrue(output.getvalue().startswith('[BaseModel] ('))

    def test_user_show(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("User.show(\"123\")")
            self.assertIn("** no instance found **", output.getvalue())

    def test_state_show_method(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("State.show(\"123\")")
            self.assertIn("** no instance found **", output.getvalue())

    def test_city_show_method(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("City.show(\"456\")")
            self.assertIn("** no instance found **", output.getvalue())

    def test_amenity_show_method(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("Amenity.show(\"789\")")
            self.assertIn("** no instance found **", output.getvalue())

    def test_place_show_method(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("Place.show(\"101\")")
            self.assertIn("** no instance found **", output.getvalue())

    def test_review_show_method(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("Review.show(\"202\")")
            self.assertIn("** no instance found **", output.getvalue())

    def test_destroy_base_model(self):
        with patch("sys.stdout", new=StringIO()) as output:
            obj = BaseModel()
            self.console.do_destroy("BaseModel " + obj.id)
            self.assertEqual(storage.all(), {})

    def test_destroy_base_model_id(self):
        with patch("sys.stdout", new=StringIO()) as output:
            obj = BaseModel()
            self.console.do_destroy("BaseModel " + obj.id)
            self.assertFalse(obj.id in storage.all().keys())

    def test_destroy_user(self):
        with patch("sys.stdout", new=StringIO()) as output:
            obj = User()
            obj_id = obj.id
            self.console.do_destroy("User " + obj_id)
            self.assertIsNone(storage.all().get("User." + obj_id))

    def test_destroy_city(self):
        with patch("sys.stdout", new=StringIO()) as output:
            obj = City()
            obj_id = obj.id
            self.console.do_destroy("City " + obj_id)
            self.assertIsNone(storage.all().get("City." + obj_id))

    def test_destroy_state(self):
        with patch("sys.stdout", new=StringIO()) as output:
            obj = State()
            obj_id = obj.id
            self.console.do_destroy("State " + obj_id)
            self.assertIsNone(storage.all().get("State." + obj_id))

    def test_destroy_place(self):
        with patch("sys.stdout", new=StringIO()) as output:
            obj = Place()
            obj_id = obj.id
            self.console.do_destroy("Place " + obj_id)
            self.assertIsNone(storage.all().get("Place." + obj_id))

    def test_destroy_amenity(self):
        with patch("sys.stdout", new=StringIO()) as output:
            obj = Amenity()
            obj_id = obj.id
            self.console.do_destroy("Amenity " + obj_id)
            self.assertIsNone(storage.all().get("Amenity." + obj_id))

    def test_destroy_review(self):
        with patch("sys.stdout", new=StringIO()) as output:
            obj = Review()
            obj_id = obj.id
            self.console.do_destroy("Review " + obj_id)
            self.assertIsNone(storage.all().get("Review." + obj_id))

    def test_all_base_model(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.do_all("BaseModel")
            self.assertIn("[]", output.getvalue())

    def test_review_all_method(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("Review.all()")
            self.assertIn("[]", output.getvalue())

    def test_state_all_method(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("State.all()")
            self.assertIn("[]", output.getvalue())

    def test_city_all_method(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("City.all()")
            self.assertIn("[]", output.getvalue())

    def test_amenity_all_method(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("Amenity.all()")
            self.assertIn("[]", output.getvalue())

    def test_place_all_method(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("Place.all()")
            self.assertIn("[]", output.getvalue())

    def test_update_base_model(self):
        with patch("sys.stdout", new=StringIO()) as output:
            obj = BaseModel()
            self.console.do_update("BaseModel " + obj.id + " name TestName")
            self.assertIn("'name': 'TestName'", str(obj))

    def test_base_model_all_method(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("BaseModel.all()")
            self.assertIn("[]", output.getvalue())

    def test_user_all_method(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("User.all()")
            self.assertIn("[]", output.getvalue())

    def test_base_model_count(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("BaseModel.count()")
            self.assertIn("0", output.getvalue())

    def test_user_count(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("User.count()")
            self.assertIn("0", output.getvalue())

    def test_state_count_method(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("State.count()")
            self.assertIn("0", output.getvalue())

    def test_city_count_method(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("City.count()")
            self.assertIn("0", output.getvalue())

    def test_amenity_count_method(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("Amenity.count()")
            self.assertIn("0", output.getvalue())

    def test_place_count_method(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("Place.count()")
            self.assertIn("0", output.getvalue())

    def test_review_count_method(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd("Review.count()")
            self.assertIn("0", output.getvalue())

    def test_state_update_method(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd('State.update("123", "name", "New Brunswick")')
            self.assertIn("** no instance found **", output.getvalue())

    def test_city_update_method(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd('City.update("456", "name", "Bogoso")')
            self.assertIn("** no instance found **", output.getvalue())

    def test_amenity_update_method(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd('Amenity.update("789", "name", "WiFi")')
            self.assertIn("** no instance found **", output.getvalue())

    def test_place_update_method(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd('Place.update("101", "name", "Cozy Cabin")')
            self.assertIn("** no instance found **", output.getvalue())

    def test_review_update_method(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd('Review.update("202", "name", "Great inspiration")')
            self.assertIn("** no instance found **", output.getvalue())

    def test_base_model_update_dict_method(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.console.onecmd('BaseModel.update("123", {"name": "Ransford"})')
            self.assertIn("** no instance found **", output.getvalue())

    def test_user_update_dict(self):
        with patch("sys.stdout", new=StringIO()) as output:
            obj = User()
            self.console.onecmd('User.update("' + obj.id + '", { "first_name": "mathew" })')
            updated_obj = storage.all()["User." + obj.id]
            self.assertEqual(updated_obj.first_name, "mathew")

    def test_state_update_dict(self):
        with patch("sys.stdout", new=StringIO()) as output:
            obj = State()
            self.console.onecmd('State.update("' + obj.id + '", { "name": "New York" })')
            updated_obj = storage.all()["State." + obj.id]
            self.assertEqual(updated_obj.name, "New York")

    def test_amenity_update_dict(self):
        with patch("sys.stdout", new=StringIO()) as output:
            obj = Amenity()
            self.console.onecmd('Amenity.update("' + obj.id + '", { "name": "Wifi" })')
            updated_obj = storage.all()["Amenity." + obj.id]
            self.assertEqual(updated_obj.name, "Wifi")

    def test_city_update_dict(self):
        with patch("sys.stdout", new=StringIO()) as output:
            obj = City()
            self.console.onecmd('City.update("' + obj.id + '", { "name": "New York" })')
            updated_obj = storage.all()["City." + obj.id]
            self.assertEqual(updated_obj.name, "New York")

    def test_place_update_dict(self):
        with patch("sys.stdout", new=StringIO()) as output:
            obj = Place()
            self.console.onecmd('Place.update("' + obj.id + '", { "name": "Luxury Suite" })')
            updated_obj = storage.all()["Place." + obj.id]
            self.assertEqual(updated_obj.name, "Luxury Suite")

    def test_review_update_dict(self):
        with patch("sys.stdout", new=StringIO()) as output:
            obj = Review()
            self.console.onecmd('Review.update("' + obj.id + '", { "text": "Great experience" })')
            updated_obj = storage.all()["Review." + obj.id]
            self.assertEqual(updated_obj.text, "Great experience")

if __name__ == '__main__':
    unittest.main()
