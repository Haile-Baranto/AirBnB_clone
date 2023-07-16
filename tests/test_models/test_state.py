#!/usr/bin/python3
"""
Unittest for State class.
"""

import unittest
import datetime
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    Test cases for State class.
    """

    def setUp(self):
        """
        Set up test fixtures.
        """
        self.state = State()

    def tearDown(self):
        """
        Tear down test fixtures.
        """
        del self.state

    def test_attributes(self):
        """
        Test attributes.

        Returns:
            None.
        """
        self.assertIsInstance(self.state.name, str)

    def test_inheritance(self):
        """
        Test inheritance.

        Returns:
            None.
        """
        self.assertTrue(issubclass(State, BaseModel))

    def test_str(self):
        """
        Test __str__ method.

        Returns:
            None.
        """
        string = "[State] ({}) {}".format(self.state.id, self.state.__dict__)
        self.assertEqual(str(self.state), string)

    def test_to_dict(self):
        """
        Test to_dict method.

        Returns:
            None.
        """
        dict_ = self.state.to_dict()
        self.assertIsInstance(dict_, dict)
        for key in dict_:
            self.assertTrue(hasattr(self.state, key))

    def test_init_kwargs(self):
         """
         Test __init__ method with **kwargs argument.

         Returns:
             None.
         """
         kwargs = {"id": "123", "created_at": "2022-07-15T15:09:33.000000",
                   "updated_at": "2022-07-15T15:09:33.000000",
                   "name": "California"}
         state = State(**kwargs)
         for key in kwargs:
             if key != "__class__":
                 self.assertTrue(hasattr(state, key))
         self.assertEqual(state.id, kwargs["id"])
         self.assertEqual(state.created_at.isoformat(),
                          kwargs["created_at"])
         self.assertEqual(state.updated_at.isoformat(),
                          kwargs["updated_at"])
         self.assertEqual(state.name, kwargs["name"])

    def test_init_args(self):
         """
         Test __init__ method with *args argument.

         Returns:
             None.
         """
         args = ["123", "2022-07-15T15:09:33.000000",
                 "2022-07-15T15:09:33.000000", "California"]
         state = State(*args)
         attrs = ["id", "created_at", "updated_at", "name"]
         for i in range(len(attrs)):
             attr = attrs[i]
             value = args[i]
             if attr == "created_at" or attr == "updated_at":
                 value = datetime.datetime.strptime(value,
                                                    "%Y-%m-%dT%H:%M:%S.%f")
             self.assertTrue(hasattr(state, attr))
             self.assertEqual(getattr(state, attr), value)

if __name__ == "__main__":
    unittest.main()