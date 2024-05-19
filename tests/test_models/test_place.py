#!/usr/bin/python3
"""
    Test Place unittest module

"""

from datetime import datetime, date
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace_object_instance(unittest.TestCase):
    """
        Test Place class object instance
    """

    def setUp(self):
        print("Testing Place Object Instance")

    def test_Place_is_a_subclass_basemodel(self):
        d1 = Place()
        self.assertIsInstance(d1, BaseModel)

    def test_Place_unique_two_id(self):
        d1 = Place()
        d2 = Place()
        self.assertNotEqual(d1.id, d2.id)

    def test_Place_unique_three_ids(self):
        d1 = Place()
        d2 = Place()
        d3 = Place()
        self.assertNotEqual(d2.id, d3.id)

    def test_Place_city_default_id(self):
        d1 = Place()
        self.assertEqual(d1.city_id, "")
        self.assertIn("city_id", dir(d1))

    def test_place_user_id_default_id(self):
        d1 = Place()
        self.assertEqual(d1.user_id, "")

    def test_name_default_value(self):
        d1 = Place()
        self.assertEqual(d1.name, "")

    def test_description_default_value(self):
        d1 = Place()
        self.assertEqual(d1.description, "")

    def test_number_rooms_default_value(self):
        d1 = Place()
        self.assertEqual(d1.number_rooms, 0)

    def test_number_bathrooms_default_value(self):
        d1 = Place()
        self.assertEqual(d1.number_bathrooms, 0)

    def test_max_guest_default_value(self):
        d1 = Place()
        self.assertEqual(d1.max_guest, 0)

    def test_price_by_night(self):
        d1 = Place()
        self.assertEqual(d1.price_by_night, 0)

    def test_latitude_default_value(self):
        d1 = Place()
        self.assertEqual(d1.latitude, 0.0)

    def test_longitude_default_value(self):
        d1 = Place()
        self.assertEqual(d1.longitude, 0.0)

    def test_place_ids_default_value(self):
        d1 = Place()
        self.assertEqual(d1.amenity_ids, [])

    def test_place_object_creation_time(self):
        d1 = Place()
        d2 = Place()
        self.assertNotEqual(d1.created_at, d2.created_at)

    def test_place_object_updated_time(self):
        d1 = Place()
        d2 = Place()
        self.assertNotEqual(d1.updated_at, d2.updated_at)


class TestPlace_Has_attr_BaseModel(unittest.TestCase):

    """
        Test Place for basemodel attributes
    """

    def setUp(self):
        print("Testing if Place has the attrs of parent")

    def test_Place_has_id_attr(self):
        d1 = Place()
        self.assertTrue(d1.id)

    def test_Place_has_created_at_attr(self):
        d1 = Place()
        self.assertTrue(d1.created_at)

    def test_place_has_updated_at_attr(self):
        d1 = Place()
        self.assertTrue(d1.updated_at)

    def test_place_has__str__attr(self):
        d1 = Place()
        self.assertTrue(d1.__str__)


if __name__ == "__main__":
    unittest.main()
