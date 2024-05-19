#!/usr/bin/python3

"""
unittests for models/engine/file_storage.py.
Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__fp))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__ob))

    def test_storage_initializes(self):
        self.assertEqual(type(models.strge), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__ob = {}

    def test_all(self):
        self.assertEqual(dict, type(models.strge.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.strge.all(None)

    def test_new(self):
        bse_mod = BaseModel()
        usrr = User()
        stat = State()
        plce = Place()
        cyy = City()
        amn = Amenity()
        reve = Review()
        models.strge.new(bse_mod)
        models.strge.new(usrr)
        models.strge.new(stat)
        models.strge.new(plce)
        models.strge.new(cyy)
        models.strge.new(amn)
        models.strge.new(reve)
        self.assertIn("BaseModel." + bse_mod.id, models.strge.all().keys())
        self.assertIn(bse_mod, models.strge.all().values())
        self.assertIn("User." + usrr.id, models.strge.all().keys())
        self.assertIn(usrr, models.strge.all().values())
        self.assertIn("State." + stat.id, models.strge.all().keys())
        self.assertIn(stat, models.strge.all().values())
        self.assertIn("Place." + plce.id, models.strge.all().keys())
        self.assertIn(plce, models.strge.all().values())
        self.assertIn("City." + cyy.id, models.strge.all().keys())
        self.assertIn(cyy, models.strge.all().values())
        self.assertIn("Amenity." + amn.id, models.strge.all().keys())
        self.assertIn(amn, models.strge.all().values())
        self.assertIn("Review." + reve.id, models.strge.all().keys())
        self.assertIn(reve, models.strge.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.strge.new(BaseModel(), 1)

    def test_save(self):
        bse_mod = BaseModel()
        usrr = User()
        stat = State()
        plce = Place()
        cyy = City()
        amn = Amenity()
        reve = Review()
        models.strge.new(bse_mod)
        models.strge.new(usrr)
        models.strge.new(stat)
        models.strge.new(plce)
        models.strge.new(cyy)
        models.strge.new(amn)
        models.strge.new(reve)
        models.strge.save()
        save = ""
        with open("file.json", "r") as f:
            save = f.read()
            self.assertIn("BaseModel." + bse_mod.id, save)
            self.assertIn("User." + usrr.id, save)
            self.assertIn("State." + stat.id, save)
            self.assertIn("Place." + plce.id, save)
            self.assertIn("City." + cyy.id, save)
            self.assertIn("Amenity." + amn.id, save)
            self.assertIn("Review." + reve.id, save)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.strge.save(None)

    def test_reload(self):
        bse_mod = BaseModel()
        usrr = User()
        stat = State()
        plce = Place()
        cyy = City()
        amn = Amenity()
        reve = Review()
        models.strge.new(bse_mod)
        models.strge.new(usrr)
        models.strge.new(stat)
        models.strge.new(plce)
        models.strge.new(cyy)
        models.strge.new(amn)
        models.strge.new(reve)
        models.strge.save()
        models.strge.reload()
        objs = FileStorage._FileStorage__ob
        self.assertIn("BaseModel." + bse_mod.id, objs)
        self.assertIn("User." + usrr.id, objs)
        self.assertIn("State." + stat.id, objs)
        self.assertIn("Place." + plce.id, objs)
        self.assertIn("City." + cyy.id, objs)
        self.assertIn("Amenity." + amn.id, objs)
        self.assertIn("Review." + reve.id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.strge.reload(None)


if __name__ == "__main__":
    unittest.main()
