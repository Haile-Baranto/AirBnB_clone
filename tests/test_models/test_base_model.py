import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Unit tests for the BaseModel class.
    """

    def setUp(self):
        """
        Set up method that is run before each individual test case.
        """
        self.model = BaseModel()

    def test_attributes_existence(self):
        """
        Test that the BaseModel instance has the required attributes.
        """
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_id_generation(self):
        """
        Test that the BaseModel instance generates a valid ID.
        """
        self.assertIsNotNone(self.model.id)
        self.assertIsInstance(self.model.id, str)

    def test_timestamps(self):
        """
        Test that the BaseModel instance has valid timestamps.
        """
        self.assertIsNotNone(self.model.created_at)
        self.assertIsNotNone(self.model.updated_at)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_string_representation(self):
        """
        Test the string representation of the BaseModel instance.
        """
        string = str(self.model)
        self.assertIn('[BaseModel]', string)
        self.assertIn(self.model.id, string)

    def test_save_updates_updated_at(self):
        """
        Test that the save() method updates the updated_at attribute.
        """
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict_returns_dictionary(self):
        """
        Test that the to_dict() method returns a dictionary.
        """
        dictionary = self.model.to_dict()
        self.assertIsInstance(dictionary, dict)

    def test_to_dict_contains_all_attributes(self):
        """
        Test that the to_dict() method contains all the required attributes.
        """
        dictionary = self.model.to_dict()
        self.assertIn('id', dictionary)
        self.assertIn('created_at', dictionary)
        self.assertIn('updated_at', dictionary)

    def test_to_dict_has_correct_values(self):
        """
        Test that the to_dict() method has correct values for attributes.
        """
        dictionary = self.model.to_dict()
        self.assertEqual(dictionary['id'], self.model.id)
        self.assertEqual(dictionary['created_at'], self.model.created_at.isoformat())
        self.assertEqual(dictionary['updated_at'], self.model.updated_at.isoformat())

    def test_to_dict_excludes_class_attribute(self):
        """
        Test that the to_dict() method excludes the class attribute.
        """
        dictionary = self.model.to_dict()
        self.assertNotIn('__class__', dictionary)

    def test_to_dict_returns_copy_of_attributes(self):
        """
        Test that modifying the dictionary returned by to_dict() doesn't
        modify the actual instance attributes.
        """
        dictionary = self.model.to_dict()
        dictionary['test_key'] = 'test_value'
        self.assertNotIn('test_key', self.model.__dict__)

    def test_attribute_assignment(self):
        """
        Test assignment of a new attribute to the BaseModel instance.
        """
        self.model.test_attribute = 'test_value'
        self.assertTrue(hasattr(self.model, 'test_attribute'))
        self.assertEqual(self.model.test_attribute, 'test_value')

    def test_initialization_with_arguments(self):
        """
        Test initialization of BaseModel with arguments.
        """
        model = BaseModel(test_attribute='test_value')
        self.assertTrue(hasattr(model, 'test_attribute'))
        self.assertEqual(model.test_attribute, 'test_value')

    def test_initialization_with_kwargs(self):
        """
        Test initialization of BaseModel with **kwargs.
        """
        model_data = {
            'id': 'test_id',
            'created_at': '2022-01-01T00:00:00.000001',
            'updated_at': '2022-01-01T00:00:00.000002',
            'test_attribute': 'test_value'
        }
        model = BaseModel(**model_data)
        self.assertEqual(model.id, 'test_id')
        self.assertEqual(model.created_at, datetime(2022, 1, 1, 0, 0, 0, 1))
        self.assertEqual(model.updated_at, datetime(2022, 1, 1, 0, 0, 0, 2))
        self.assertEqual(model.test_attribute, 'test_value')

    def test_id_uniqueness(self):
        """
        Test the uniqueness of the ID generated for BaseModel instances.
        """
        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)

    def test_created_at_immutable(self):
        """
        Test that the created_at attribute is immutable.
        """
        with self.assertRaises(AttributeError):
            setattr(self.model, 'created_at', datetime.now())

    def test_updated_at_immutable(self):
        """
        Test that the updated_at attribute is immutable.
        """
        with self.assertRaises(AttributeError):
            setattr(self.model, 'updated_at', datetime.now())

    def test_str_representation_with_attributes(self):
        """
        Test string representation of BaseModel instance with attributes.
        """
        self.model.test_attribute = 'test_value'
        string = str(self.model)
        self.assertIn('test_attribute', string)
        self.assertIn('test_value', string)

    def test_str_representation_without_attributes(self):
        """
        Test string representation of BaseModel instance without attributes.
        """
        string = str(self.model)
        self.assertNotIn('test_attribute', string)

    def test_save_does_not_update_created_at(self):
        """
        Test that the save() method does not update the created_at attribute.
        """
        old_created_at = self.model.created_at
        self.model.save()
        self.assertEqual(old_created_at, self.model.created_at)

    def test_to_dict_does_not_include_private_attributes(self):
        """
        Test that the to_dict() method does not include private attributes.
        """
        self.model._private_attribute = 'private_value'
        dictionary = self.model.to_dict()
        self.assertNotIn('_private_attribute', dictionary)

    def test_to_dict_includes_additional_attributes(self):
        """
        Test that the to_dict() method includes additional attributes.
        """
        self.model.additional_attribute = 'additional_value'
        dictionary = self.model.to_dict()
        self.assertIn('additional_attribute', dictionary)
        self.assertEqual(dictionary['additional_attribute'], 'additional_value')

    def test_initialization_with_invalid_timestamps(self):
        """
        Test initialization of BaseModel with invalid timestamps.
        """
        model_data = {
            'id': 'test_id',
            'created_at': 'invalid_timestamp',
            'updated_at': 'invalid_timestamp'
        }
        with self.assertRaises(ValueError):
            BaseModel(**model_data)


if __name__ == '__main__':
    unittest.main()