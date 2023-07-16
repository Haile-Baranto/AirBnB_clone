import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_city_inheritance(self):
        """Test that City inherits from BaseModel."""
        self.assertIsInstance(City(), BaseModel)

    def test_city_attributes(self):
        """Test the attributes of the City class."""
        city = City()

        # Test the public class attributes
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_attribute_types(self):
        """Test the types of the attributes in the City class."""
        city = City()

        # Test attribute types
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)

    def test_city_attribute_defaults(self):
        """Test the default values of the attributes in the City class."""
        city = City()

        # Test default attribute values
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()