#!/usr/bin/python3
"""
Unittest for User class.
"""

import unittest
from models.user import User
import datetime


class TestUser(unittest.TestCase):
    """
    Test cases for User class.
    """

    def setUp(self):
        """
        Set up test fixtures.
        """
        self.user = User()

    def tearDown(self):
        """
        Tear down test fixtures.
        """
        del self.user

    def test_attributes(self):
        """
        Test attributes.

        Returns:
            None.
        """
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_inheritance(self):
        """
        Test inheritance.

        Returns:
            None.
        """
        self.assertTrue(issubclass(User, BaseModel))

    def test_str(self):
        """
        Test __str__ method.

        Returns:
            None.
        """
        string = "[User] ({}) {}".format(self.user.id, self.user.__dict__)
        self.assertEqual(str(self.user), string)

    def test_to_dict(self):
        """
        Test to_dict method.

        Returns:
            None.
        """
        dict_ = self.user.to_dict()
        self.assertIsInstance(dict_, dict)
        for key in dict_:
            self.assertTrue(hasattr(self.user, key))

    def test_init_kwargs(self):
        """
         Test __init__ method with **kwargs argument.

         Returns:
             None.
         """
        kwargs = {"id": "123", "created_at": "2022-07-15T15:09:33.000000",
                   "updated_at": "2022-07-15T15:09:33.000000",
                   "email": "test@test.com", "password": "test",
                   "first_name": "Test", "last_name": "Test"}
        user = User(**kwargs)
        for key in kwargs:
             if key != "__class__":
                 self.assertTrue(hasattr(user, key))
        self.assertEqual(user.id, kwargs["id"])
        self.assertEqual(user.created_at.isoformat(),
                          kwargs["created_at"])
        self.assertEqual(user.updated_at.isoformat(),
                          kwargs["updated_at"])
        self.assertEqual(user.email, kwargs["email"])
        self.assertEqual(user.password, kwargs["password"])
        self.assertEqual(user.first_name, kwargs["first_name"])
        self.assertEqual(user.last_name, kwargs["last_name"])

    def test_init_args(self):
         """
         Test __init__ method with *args argument.

         Returns:
             None.
         """
         args = ["123", "2022-07-15T15:09:33.000000",
                 "2022-07-15T15:09:33.000000",
                 "test@test.com", "test", "Test", "Test"]
         user = User(*args)
         attrs = ["id", "created_at", "updated_at",
                  "email", "password", "first_name", "last_name"]
         for i in range(len(attrs)):
             attr = attrs[i]
             value = args[i]
             if attr == "created_at" or attr == "updated_at":
                 value = datetime.datetime.strptime(value,
                                                    "%Y-%m-%dT%H:%M:%S.%f")
             self.assertTrue(hasattr(user, attr))
             self.assertEqual(getattr(user, attr), value)

if __name__ == "__main__":
    unittest.main()