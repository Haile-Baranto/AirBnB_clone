import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Set up the test environment."""
        self.file_path = "file.json"
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up the test environment."""
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_attributes(self):
        """Test the attributes of the FileStorage class."""
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all(self):
        """Test the all() method of the FileStorage class."""
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(all_objects, self.storage._FileStorage__objects)

    def test_new(self):
        """Test the new() method of the FileStorage class."""
        obj = BaseModel()
        self.storage.new(obj)
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(obj_key, self.storage._FileStorage__objects)
        self.assertEqual(self.storage._FileStorage__objects[obj_key], obj)

    def test_save(self):
        """Test the save() method of the FileStorage class."""
        obj = BaseModel()
        self.storage.new(obj)
        with patch("builtins.open", create=True) as mock_open:
            self.storage.save()
            mock_open.assert_called_once_with(self.file_path, "w")
            mock_open.return_value.__enter__.return_value.write.assert_called_once()

    def test_reload_file_not_found(self):
        """Test the reload() method when the file doesn't exist."""
        with patch("builtins.open", side_effect=FileNotFoundError):
            self.storage.reload()

    def test_reload(self):
        """Test the reload() method of the FileStorage class."""
        obj = BaseModel()
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.storage._FileStorage__objects[obj_key] = obj
        obj.to_dict = lambda: {"key": "value"}

        with patch("builtins.open", create=True) as mock_open:
            mock_open.return_value.__enter__.return_value.read.return_value = \
                '{"BaseModel.123": {"key": "value"}}'
            self.storage.reload()

        self.assertIn(obj_key, self.storage._FileStorage__objects)
        self.assertIsInstance(self.storage._FileStorage__objects[obj_key], BaseModel)
        self.assertEqual(self.storage._FileStorage__objects[obj_key].key, "value")

    def test_reload_invalid_class_name(self):
        """Test the reload() method with an invalid class name."""
        with patch("builtins.open", create=True) as mock_open:
            mock_open.return_value.__enter__.return_value.read.return_value = \
                '{"InvalidClass.123": {"key": "value"}}'
            self.storage.reload()

        self.assertEqual(len(self.storage._FileStorage__objects), 0)

    # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()