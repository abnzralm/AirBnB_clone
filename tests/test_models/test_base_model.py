#!/usr/bin/python3
""" Unittest test module for base model module
    """

import os
from datetime import datetime, date
import unittest
from models.base_model import BaseModel
from time import sleep
import os


class TestBaseModel_Object_instance(unittest.TestCase):
    """ Test Base Model Object Instance

    Args:
        unittest (module): unittest module
    """

    def setUp(self):
        print("Testing ... Base Obj inst")

    def test_object_isinstance(self):
        y1 = BaseModel()
        self.assertIsInstance(y1, BaseModel)

    def test_object_instance_not_equal(self):
        y1 = BaseModel()
        y2 = BaseModel()
        self.assertNotEqual(y1, y2)

    def test_object_instance_unique_ids(self):
        y1 = BaseModel()
        y2 = BaseModel()
        self.assertNotEqual(y1.id, y2.id)

    def test_object_instance_creation_time(self):
        self.assertNotEqual(datetime.now(), BaseModel().created_at)

    def test_object_instance_updated_time(self):
        self.assertNotEqual(datetime.now(), BaseModel().updated_at)

    def test_object_instance_sameday_creation(self):
        self.assertEqual(date.today().strftime("%d/%m/%Y"),
                         BaseModel().created_at.strftime("%d/%m/%Y"))

    def test_kwargs_param1(self):
        y3 = BaseModel(name="Shiferaw")
        self.assertEqual(y3.name, "Shiferaw")

    def test_kwargs_param2(self):
        y3 = BaseModel(name="Shiferaw", partner="Kidus")
        self.assertEqual(y3.partner, "Kidus")

    def test_unique_ids(self):
        y1 = BaseModel()
        y2 = BaseModel()
        self.assertNotEqual(y1.id, y2.id)

    def test_object_ids_type(self):
        y1 = BaseModel()
        self.assertEqual(str, type(y1.id))

    def test_object_ids_list(self):
        y2 = BaseModel()
        self.assertNotEqual(list,  type(y2.id))

    def test_object_ids_tuple(self):
        y1 = BaseModel()
        self.assertNotEqual(tuple, type(y1.id))

    def test_object_ids_bool(self):
        y2 = BaseModel()
        self.assertNotEqual(bool,  type(y2.id))

    def test_object_ids_None(self):
        y2 = BaseModel()
        self.assertNotEqual(None,  type(y2.id))

    def test_object_ids_float(self):
        y2 = BaseModel()
        self.assertNotEqual(float, type(y2.id))

    def test_object_ids_int(self):
        y1 = BaseModel()
        self.assertNotEqual(int, type(y1.id))

    def test_object_ids_dict(self):
        y2 = BaseModel()
        self.assertNotEqual(dict,  type(y2.id))

    def test_object_ids_complex(self):
        y2 = BaseModel()
        self.assertNotEqual(complex, type(y2.id))

    def test_object_ids_set(self):
        y2 = BaseModel()
        self.assertNotEqual(set, type(y2.id))

    def test_object_ids_frozenset(self):
        y2 = BaseModel()
        self.assertNotEqual(frozenset, type(y2.id))

    def test_object_ids_range(self):
        y2 = BaseModel()
        self.assertNotEqual(range, type(y2.id))

    def test_object_ids_bytes(self):
        y2 = BaseModel()
        self.assertNotEqual(bytes, type(y2.id))

    def test_object_ids_bytearray(self):
        y2 = BaseModel()
        self.assertNotEqual(bytearray, type(y2.id))

    def test_object_ids_memoryview(self):
        y2 = BaseModel()
        self.assertNotEqual(memoryview, type(y2.id))

    def test_object_str_representation(self):
        y1 = BaseModel()
        self.assertIn("[BaseModel]", y1.__str__())

    def test_to_dict_name(self):
        b = BaseModel()
        b.name = "My dict"
        d = b.to_dict()
        self.assertEqual(d["name"], b.name)

    def test_to_dict_age(self):
        y1 = BaseModel()
        y1.age = 16
        d = y1.to_dict()
        self.assertEqual(d["age"], y1.age)

    def test_to_dict_id(self):
        b = BaseModel()
        d = b.to_dict()
        self.assertEqual(d["id"], b.id)

    def test_to_dict_created_at(self):
        b = BaseModel()
        d = b.to_dict()
        self.assertEqual(d["created_at"], b.created_at.isoformat())

    def test_to_dict_updated_at(self):
        b = BaseModel()
        d = b.to_dict()
        self.assertEqual(d["updated_at"], b.updated_at.isoformat())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_type(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_type(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_uniq_ids(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_diff_created_at(self):
        o1 = BaseModel()
        sleep(0.05)
        o2 = BaseModel()
        self.assertLess(o1.created_at, o2.created_at)

    def test_diff_updated_at(self):
        o1 = BaseModel()
        sleep(0.05)
        o2 = BaseModel()
        self.assertLess(o1.updated_at, o2.updated_at)\



class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

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

    def test_one_save(self):
        bse_mod = BaseModel()
        sleep(0.05)
        first_updated_at = bse_mod.updated_at
        bse_mod.save()
        self.assertLess(first_updated_at, bse_mod.updated_at)

    def test_two_saves(self):
        bse_mod = BaseModel()
        sleep(0.05)
        first_updated_at = bse_mod.updated_at
        bse_mod.save()
        second_updated_at = bse_mod.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bse_mod.save()
        self.assertLess(second_updated_at, bse_mod.updated_at)

    def test_save_with_arg(self):
        bse_mod = BaseModel()
        with self.assertRaises(TypeError):
            bse_mod.save(None)

    def test_save_updates_file(self):
        bse_mod = BaseModel()
        bse_mod.save()
        bmid = "BaseModel." + bse_mod.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        bse_mod = BaseModel()
        self.assertTrue(dict, type(bse_mod.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        bse_mod = BaseModel()
        self.assertIn("id", bse_mod.to_dict())
        self.assertIn("created_at", bse_mod.to_dict())
        self.assertIn("updated_at", bse_mod.to_dict())
        self.assertIn("__class__", bse_mod.to_dict())

    def test_to_dict_contains_added_attributes(self):
        bse_mod = BaseModel()
        bse_mod.name = "Holberton"
        bse_mod.my_number = 98
        self.assertIn("name", bse_mod.to_dict())
        self.assertIn("my_number", bse_mod.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        bse_mod = BaseModel()
        bm_dict = bse_mod.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        bse_mod = BaseModel()
        bse_mod.id = "123456"
        bse_mod.created_at = bse_mod.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bse_mod.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        bse_mod = BaseModel()
        self.assertNotEqual(bse_mod.to_dict(), bse_mod.__dict__)

    def test_to_dict_with_arg(self):
        bse_mod = BaseModel()
        with self.assertRaises(TypeError):
            bse_mod.to_dict(None)


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

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

    def test_one_save(self):
        bse_mod = BaseModel()
        sleep(0.05)
        first_updated_at = bse_mod.updated_at
        bse_mod.save()
        self.assertLess(first_updated_at, bse_mod.updated_at)

    def test_two_saves(self):
        bse_mod = BaseModel()
        sleep(0.05)
        first_updated_at = bse_mod.updated_at
        bse_mod.save()
        second_updated_at = bse_mod.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bse_mod.save()
        self.assertLess(second_updated_at, bse_mod.updated_at)

    def test_save_with_arg(self):
        bse_mod = BaseModel()
        with self.assertRaises(TypeError):
            bse_mod.save(None)

    def test_save_updates_file(self):
        bse_mod = BaseModel()
        bse_mod.save()
        bmid = "BaseModel." + bse_mod.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        bse_mod = BaseModel()
        self.assertTrue(dict, type(bse_mod.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        bse_mod = BaseModel()
        self.assertIn("id", bse_mod.to_dict())
        self.assertIn("created_at", bse_mod.to_dict())
        self.assertIn("updated_at", bse_mod.to_dict())
        self.assertIn("__class__", bse_mod.to_dict())

    def test_to_dict_contains_added_attributes(self):
        bse_mod = BaseModel()
        bse_mod.name = "Holberton"
        bse_mod.my_number = 98
        self.assertIn("name", bse_mod.to_dict())
        self.assertIn("my_number", bse_mod.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        bse_mod = BaseModel()
        bm_dict = bse_mod.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        bse_mod = BaseModel()
        bse_mod.id = "123456"
        bse_mod.created_at = bse_mod.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bse_mod.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        bse_mod = BaseModel()
        self.assertNotEqual(bse_mod.to_dict(), bse_mod.__dict__)

    def test_to_dict_with_arg(self):
        bse_mod = BaseModel()
        with self.assertRaises(TypeError):
            bse_mod.to_dict(None)


if __name__ == "__main__":
    unittest.main()
