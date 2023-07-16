#!/usr/bin/python3
"""
The console v: 0.0.1
Contains the entry point of the command interpreter
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

    def help_quit(self):
        """
        Display help for the quit command.
        """
        print("Quit command to exit the program")

    def help_EOF(self):
        """
        Display help for the EOF command.
        """
        print("EOF command to exit the program")

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
