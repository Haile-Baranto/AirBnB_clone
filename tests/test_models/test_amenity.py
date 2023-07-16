import unittest
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def setUp(self):
        """Set up the Amenity instance before each test."""
        self.amenity = Amenity()

    def test_inheritance(self):
        """Test if Amenity inherits from BaseModel."""
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes(self):
        """Test the existence of required attributes."""
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_name_default_value(self):
        """Test the default value of the name attribute."""
        self.assertEqual(self.amenity.name, "")

    def test_name_assignment(self):
        """Test assigning a value to the name attribute."""
        self.amenity.name = "Swimming Pool"
        self.assertEqual(self.amenity.name, "Swimming Pool")

    def test_to_dict_returns_dictionary(self):
        """Test if to_dict() method returns a dictionary."""
        dictionary = self.amenity.to_dict()
        self.assertIsInstance(dictionary, dict)

    def test_to_dict_contains_all_attributes(self):
        """Test if to_dict() includes all the required attributes."""
        dictionary = self.amenity.to_dict()
        self.assertIn('id', dictionary)
        self.assertIn('created_at', dictionary)
        self.assertIn('updated_at', dictionary)
        self.assertIn('name', dictionary)

    def test_to_dict_has_correct_values(self):
        """Test if to_dict() contains correct attribute values."""
        self.amenity.name = "Gym"
        dictionary = self.amenity.to_dict()
        self.assertEqual(dictionary['name'], "Gym")

    def test_to_dict_excludes_class_attribute(self):
        """Test if to_dict() excludes the '__class__' attribute."""
        dictionary = self.amenity.to_dict()
        self.assertNotIn('__class__', dictionary)

    def test_to_dict_returns_copy_of_attributes(self):
        """Test if to_dict() returns a copy of the attributes."""
        dictionary = self.amenity.to_dict()
        dictionary['test_key'] = 'test_value'
        self.assertNotIn('test_key', self.amenity.__dict__)

    def test_str_representation(self):
        """Test the string representation of the Amenity instance."""
        string = str(self.amenity)
        self.assertIn("[Amenity]", string)
        self.assertIn(self.amenity.id, string)
        self.assertIn(self.amenity.name, string)

    def test_initialization_with_arguments(self):
        """Test initialization of Amenity with arguments."""
        amenity = Amenity(name="Test Amenity")
        self.assertEqual(amenity.name, "Test Amenity")

    def test_initialization_with_kwargs(self):
        """Test initialization of Amenity with kwargs."""
        amenity_data = {
            'id': 'test_id',
            'created_at': '2022-01-01T00:00:00.000001',
            'updated_at': '2022-01-01T00:00:00.000002',
            'name': 'Test Amenity'
        }
        amenity = Amenity(**amenity_data)
        self.assertEqual(amenity.id, 'test_id')
        self.assertEqual(amenity.created_at, datetime(2022, 1, 1, 0, 0, 0, 1))
        self.assertEqual(amenity.updated_at, datetime(2022, 1, 1, 0, 0, 0, 2))
        self.assertEqual(amenity.name, 'Test Amenity')

    def test_id_uniqueness(self):
        """Test the uniqueness of the id attribute."""
        amenity2 = Amenity()
        self.assertNotEqual(self.amenity.id, amenity2.id)

    def test_created_at_immutable(self):
        """Test immutability of the created_at attribute."""
        with self.assertRaises(AttributeError):
            self.amenity.created_at = datetime.now()

    def test_updated_at_immutable(self):
        """Test immutability of the updated_at attribute."""
        with self.assertRaises(AttributeError):
            self.amenity.updated_at = datetime.now()

    def test_save_updates_updated_at(self):
        """Test if save() method updates the updated_at attribute."""
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(old_updated_at, self.amenity.updated_at)


if __name__ == '__main__':
    unittest.main()