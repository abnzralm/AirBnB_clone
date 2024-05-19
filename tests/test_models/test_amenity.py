#!/usr/bin/python3
"""
    Test User unittest module
"""

from datetime import datetime, date
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity_object_instance(unittest.TestCase):

    """
        Test amenity class object instance
    """

    def setUp(self):
        print("Testing Amenity Object Instance")

    def test_Amenity_is_a_subclass_basemodel(self):
        z1 = Amenity()
        self.assertIsInstance(z1, BaseModel)

    def test_Amenity_is_instabce(self):
        z1 = Amenity()
        self.assertIsInstance(z1, Amenity)

    def test_Amenity_two_ids(self):
        z1 = Amenity()
        z2 = Amenity()
        self.assertNotEqual(z1.id, z2.id)

    def test_Amenity_three_ids(self):
        z1 = Amenity()
        z2 = Amenity()
        z3 = Amenity()
        self.assertNotEqual(z3.id, z1.id)

    def test_Amenity_created_time(self):
        z1 = Amenity()
        z2 = Amenity()
        self.assertNotEqual(z1.created_at, z2.created_at)

    def test_Amenity_updated_time(self):
        z1 = Amenity()
        z2 = Amenity()
        self.assertNotEqual(z1.updated_at, z2.updated_at)

    def test_Amenity_nameid_default_value(self):
        z1 = Amenity()
        self.assertEqual(z1.name, "")


class TestAmenity_Has_attr_basemodel(unittest.TestCase):
    """
        Test Amenity for basemodel attributes
    """

    def setUp(self):
        print("Testing if Amenity has the attrs of parent")

    def test_Amenity_has_id_attr(self):
        z1 = Amenity()
        self.assertTrue(z1.id)

    def test_Amenity_has_created_at_attr(self):
        z1 = Amenity()
        self.assertTrue(z1.created_at)

    def test_Amenity_has_updated_at_attr(self):
        z1 = Amenity()
        self.assertTrue(z1.created_at)

    def test_Amenity_has__str___attr(self):
        z1 = Amenity()
        self.assertTrue(z1.__str__)

    def test_Amenity_has_save_attr(self):
        z1 = Amenity()
        self.assertTrue(z1.save)

    def test_Amenity_has_to_dict_attr(self):
        al = Amenity()
        self.assertTrue(al.to_dict)

    def test_Amenity_can_take_kwargs(self):
        z2 = Amenity(name="Shiferaw")
        self.assertEqual(z2.name, "Shiferaw")


if __name__ == "__main__":
    unittest.main()
