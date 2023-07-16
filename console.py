#!/usr/bin/python3
"""
The console v: 0.0.1
Contains the entry point of the command interpreter.
"""
import cmd
import json
import re
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Custom console class
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, saves it (to the JSON file),
        and prints the id.

        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
        elif arg not in ["BaseModel", "User", "State", "City",
                         "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class
        name and id.

        Usage: show <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "State", "City",
                             "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = args[0] + "." + args[1]
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.

        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "State", "City",
                             "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = args[0] + "." + args[1]
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the
        class name.

        Usage: all [class name]
        """
        args = arg.split()
        all_objs = storage.all()
        if not args:
            print([str(obj) for obj in all_objs.values()])
        elif args[0] not in ["BaseModel", "User", "State", "City",
                             "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
        else:
            print([str(obj) for obj in all_objs.values()
                   if args[0] in obj.__class__.__name__])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating an attribute.

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "State", "City", "Amenity",
                             "Place", "Review"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = args[0] + "." + args[1]
            if key not in all_objs:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj = all_objs[key]
                attr_name = args[2]
                attr_value = args[3]
                setattr(obj, attr_name, attr_value)
                obj.save()

    def default(self, line):
        """
        Handle custom commands.
        """
        # Regex pattern to match update command with attribute value
        # in double quotes
        pattern = r'^update\s+(\w+)\s+(\w+)\s+(\w+)\s+"(.+)"$'

        match = re.match(pattern, line)
        if match:
            class_name = match.group(1)
            id = match.group(2)
            attribute = match.group(3)
            value = match.group(4)

            all_objs = storage.all()
            key = class_name + "." + id
            if key not in all_objs:
                print("** no instance found **")
            else:
                obj = all_objs[key]
                setattr(obj, attribute, value)
                obj.save()
        else:
            super().default(line)

    def help_quit(self):
        """
        Display help for the quit command.

        Usage: quit
        """
        print("Quit command to exit the program.")

    def help_EOF(self):
        """
        Display help for the EOF command.

        Usage: EOF
        """
        print("EOF command to exit the program.")

    def help_create(self):
        """
        Display help for the create command.

        Usage: create <class name>
        """
        print("Create a new instance of a class and save it to the JSON file.")

    def help_show(self):
        """
        Display help for the show command.

        Usage: show <class name> <id>
        """
        print("Print the string representation of an instance\
            based on the class name and id.")

    def help_destroy(self):
        """
        Display help for the destroy command.

        Usage: destroy <class name> <id>
        """
        print("Delete an instance based on the class name and id.")

    def help_all(self):
        """
        Display help for the all command.

        Usage: all [class name]
        """
        print("Print all string representations of instances,\
            optionally filtered by class name.")

    def help_update(self):
        """
        Display help for the update command.

        Usage: update <class name> <id> <attribute name> <attribute value>
        """
        print("Update an instance based on the class name and id by\
              adding or updating an attribute.")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
