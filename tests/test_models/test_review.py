#!/usr/bin/python3
""" Test User Unittest module
"""

from datetime import datetime, date
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview_Object_instance(unittest.TestCase):
    """ Test review class object instance
    """

    def setUp(self):
        print("Testing Review Object Instance")

    def test_Review_is_a_sublass_basemodel(self):
        g1 = Review()
        self.assertIsInstance(g1, BaseModel)

    def test_review_unique_ids(self):
        g1 = Review()
        g2 = Review()
        self.assertNotEqual(g1.id, g2.id)

    def test_review_placeid_default_value(self):
        g1 = Review()
        self.assertEqual(g1.place_id, "")

    def test_review_user_id_default_value(self):
        g1 = Review()
        self.assertEqual(g1.user_id, "")

    def test_review_text_default_value(self):
        g1 = Review()
        self.assertEqual(g1.text, "")

    def test_review_id_type(self):
        g1 = Review()
        self.assertEqual(type(g1.id), str)

    def test_review_place_id_type(self):
        g1 = Review()
        self.assertEqual(type(g1.place_id), str)

    def test_review_user_id_type(self):
        g1 = Review()
        self.assertEqual(type(g1.user_id), str)

    def test_review_object_creation_time(self):
        g1 = Review()
        g2 = Review()
        self.assertNotEqual(g1.created_at, g2.created_at)


class TestReview_Has_attr_basemodel(unittest.TestCase):

    """ Test User for super class attributes
    """

    def setUp(self):
        print("Testing if Review has the attrs of parent")

    def test_review_has_id_attr(self):
        g1 = Review()
        self.assertTrue(g1.id)

    def test_review_has_created_at_attr(self):
        g1 = Review()
        self.assertTrue(g1.created_at)

    def test_review_has_updated_at_attr(self):
        g1 = Review()
        self.assertTrue(g1.updated_at)

    def test_review_has___str__(self):
        g1 = Review()
        self.assertTrue(g1.__str__)

    def test_review_has_save_attr(self):
        g2 = Review()
        self.assertTrue(g2.save)

    def test_review_has_to_dict_attr(self):
        g1 = Review()
        self.assertTrue(g1.to_dict)

    def test_review_can_take_kwargs(self):
        g2 = Review(name="Shiferaw")
        self.assertEqual(g2.name, "Shiferaw")

    def test_review_can_take_multiple_kwargs(self):
        g2 = Review(name="Shiferaw", partner="Kidus")
        self.assertEqual(g2.partner, "Kidus")

    def test_review_object_str_representation(self):
        g1 = Review()
        self.assertIn("[Review]", g1.__str__())


if __name__ == "__main__":
    unittest.main()
