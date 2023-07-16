import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNBCommand class."""

    def setUp(self):
        """Set up the HBNBCommand instance before each test."""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up resources after each test."""
        self.console = None

    def test_quit_command(self):
        """Test the quit command."""
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    def test_EOF_command(self):
        """Test the EOF command."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("EOF")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "")

    def test_create_command_missing_class_name(self):
        """Test the create command with missing class name."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("create")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_create_command_invalid_class_name(self):
        """Test the create command with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("create InvalidClass")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_create_command_base_model(self):
        """Test the create command with BaseModel."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            storage.reload()
            obj_id = output
            obj = storage.all()['BaseModel.' + obj_id]
            self.assertIsInstance(obj, BaseModel)

    # Add more test cases for the remaining commands

    def test_count_command_missing_class_name(self):
        """Test the count command with missing class name."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("count")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_count_command_invalid_class_name(self):
        """Test the count command with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("count InvalidClass")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_count_command_valid_class_name(self):
        """Test the count command with a valid class name."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("count BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "0")

    def test_show_command_missing_class_name(self):
        """Test the show command with missing class name."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("show")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_show_command_invalid_class_name(self):
        """Test the show command with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("show InvalidClass")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_command_missing_instance_id(self):
        """Test the show command with missing instance id."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("show BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_show_command_invalid_instance_id(self):
        """Test the show command with invalid instance id."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("show BaseModel 123")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_show_command_valid_instance(self):
        """Test the show command with a valid instance."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            obj = BaseModel()
            obj.save()
            obj_id = obj.id
            self.console.onecmd("show BaseModel {}".format(obj_id))
            output = mock_stdout.getvalue().strip()
            expected_output = str(obj)
            self.assertEqual(output, expected_output)

    def test_destroy_command_missing_class_name(self):
        """Test the destroy command with missing class name."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("destroy")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_destroy_command_invalid_class_name(self):
        """Test the destroy command with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("destroy InvalidClass")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_command_missing_instance_id(self):
        """Test the destroy command with missing instance id."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("destroy BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_destroy_command_invalid_instance_id(self):
        """Test the destroy command with invalid instance id."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("destroy BaseModel 123")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_destroy_command_valid_instance(self):
        """Test the destroy command with a valid instance."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            obj = BaseModel()
            obj.save()
            obj_id = obj.id
            self.console.onecmd("destroy BaseModel {}".format(obj_id))
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "")
            self.assertNotIn('BaseModel.{}'.format(obj_id), storage.all())

    def test_all_command_invalid_class_name(self):
        """Test the all command with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("all InvalidClass")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_all_command_no_instances(self):
        """Test the all command with no instances."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("all")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "[]")

    def test_all_command_with_instances(self):
        """Test the all command with instances."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            obj1 = BaseModel()
            obj1.save()
            obj2 = BaseModel()
            obj2.save()
            self.console.onecmd("all")
            output = mock_stdout.getvalue().strip()
            expected_output = "[{}, {}]".format(obj1, obj2)
            self.assertEqual(output, expected_output)

    def test_update_command_missing_class_name(self):
        """Test the update command with missing class name."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("update")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_update_command_invalid_class_name(self):
        """Test the update command with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("update InvalidClass")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_update_command_missing_instance_id(self):
        """Test the update command with missing instance id."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("update BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_update_command_invalid_instance_id(self):
        """Test the update command with invalid instance id."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("update BaseModel 123")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_update_command_missing_attribute_name(self):
        """Test the update command with missing attribute name."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            obj = BaseModel()
            obj.save()
            obj_id = obj.id
            self.console.onecmd("update BaseModel {} ".format(obj_id))
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** attribute name missing **")

    def test_update_command_missing_attribute_value(self):
        """Test the update command with missing attribute value."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            obj = BaseModel()
            obj.save()
            obj_id = obj.id
            self.console.onecmd("update BaseModel {} attribute_name".format(obj_id))
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** value missing **")

    def test_update_command_valid_instance(self):
        """Test the update command with a valid instance."""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            obj = BaseModel()
            obj.save()
            obj_id = obj.id
            self.console.onecmd("update BaseModel {} name 'New Name'".format(obj_id))
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "")
            updated_obj = storage.all()['BaseModel.' + obj_id]
            self.assertEqual(updated_obj.name, 'New Name')


if __name__ == '__main__':
    unittest.main()