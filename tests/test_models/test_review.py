#!/usr/bin/python3
"""
Unittest for Review class.
"""

import unittest
import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test cases for Review class.
    """

    def setUp(self):
        """
        Set up test fixtures.
        """
        self.review = Review()

    def tearDown(self):
        """
        Tear down test fixtures.
        """
        del self.review

    def test_attributes(self):
        """
        Test attributes.

        Returns:
            None.
        """
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)

    def test_inheritance(self):
        """
        Test inheritance.

        Returns:
            None.
        """
        self.assertTrue(issubclass(Review, BaseModel))

    def test_str(self):
        """
        Test __str__ method.

        Returns:
            None.
        """
        string = "[Review] ({}) {}".format(self.review.id, self.review.__dict__)
        self.assertEqual(str(self.review), string)

    def test_to_dict(self):
        """
        Test to_dict method.

        Returns:
            None.
        """
        dict_ = self.review.to_dict()
        self.assertIsInstance(dict_, dict)
        for key in dict_:
            self.assertTrue(hasattr(self.review, key))

    def test_init_kwargs(self):
         """
         Test __init__ method with **kwargs argument.

         Returns:
             None.
         """
         kwargs = {"id": "123", "created_at": "2022-07-15T15:09:33.000000",
                   "updated_at": "2022-07-15T15:09:33.000000",
                   "place_id": "123", "user_id": "123", "text": "test"}
         review = Review(**kwargs)
         for key in kwargs:
             if key != "__class__":
                 self.assertTrue(hasattr(review, key))
         self.assertEqual(review.id, kwargs["id"])
         self.assertEqual(review.created_at.isoformat(),
                          kwargs["created_at"])
         self.assertEqual(review.updated_at.isoformat(),
                          kwargs["updated_at"])
         self.assertEqual(review.place_id, kwargs["place_id"])
         self.assertEqual(review.user_id, kwargs["user_id"])
         self.assertEqual(review.text, kwargs["text"])

    def test_init_args(self):
         """
         Test __init__ method with *args argument.

         Returns:
             None.
         """
         args = ["123", "2022-07-15T15:09:33.000000",
                 "2022-07-15T15:09:33.000000", "123", "123", "test"]
         review = Review(*args)
         attrs = ["id", "created_at", "updated_at",
                  "place_id", "user_id", "text"]
         for i in range(len(attrs)):
             attr = attrs[i]
             value = args[i]
             if attr == "created_at" or attr == "updated_at":
                 value = datetime.datetime.strptime(value,
                                                    "%Y-%m-%dT%H:%M:%S.%f")
             self.assertTrue(hasattr(review, attr))
             self.assertEqual(getattr(review, attr), value)

if __name__ == "__main__":
    unittest.main()