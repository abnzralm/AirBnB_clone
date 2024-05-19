#!/usr/bin/python3
"""
    Test City unittest module
"""

from datetime import datetime, date
import unittest
from models.city import City
from models.base_model import BaseModel


class Test_City_object_instance(unittest.TestCase):
    """ Test City class object instance"""

    def setUp(self):
        print("Testing ... City object instance")

    def test_city_is_a_subclass_basemodel(self):
        x1 = City()
        self.assertIsInstance(x1, BaseModel)

    def test_city_two_id(self):
        x1 = City()
        x2 = City()
        self.assertNotEqual(x1.id, x2.id)

    def test_city_three_ids(self):
        x1 = City()
        x2 = City()
        x3 = City()
        self.assertNotEqual(x2.id, x3.id)

    def test_id_type(self):
        x1 = City()
        self.assertEqual(type(x1.id), str)

    def test_created_at_time(self):
        x1 = City()
        self.assertNotEqual(datetime.now(), x1.created_at)

    def test_updated_at_time(self):
        x1 = City()
        x2 = City()
        self.assertNotEqual(x1.updated_at, x2.updated_at)

    def test_state_id_value(self):
        x1 = City()
        self.assertEqual(x1.state_id, "")

    def test_name(self):
        x1 = City()
        self.assertEqual(x1.name, "")


class TestCity_Has_Attr_basemodel(unittest.TestCase):
    """
            Test City for basemodel attributes
    """

    def setUp(self):
        print("Testing ... if City has the attributes of parent")

    def test_city_has_id_attr(self):
        x1 = City()
        self.assertTrue(x1.id)

    def test_city_has_created_at_attr(self):
        x1 = City()
        self.assertTrue(x1.created_at)

    def test_city_has_updated_at_attr(self):
        x1 = City()
        self.assertTrue(x1.updated_at)

    def test_city_has___str__attr(self):
        x1 = City()
        self.assertTrue(x1.__str__)

    def test_city_has_to_dict_attr(self):
        x1 = City()
        self.assertTrue(x1.to_dict)

    def test_City_kwargs(self):
        x1 = City(name="barkot")
        self.assertEqual(x1.name, "barkot")


if __name__ == "__main__":
    unittest.main()
