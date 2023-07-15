#!/usr/bin/python3
"""
Module: user

This module defines the User class, which inherits from BaseModel
and represents a user in the system.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel and represents
    a user in the system.

    Public Class Attributes:
        email (str): User's email address.
        password (str): User's password.
        first_name (str): User's first name.
        last_name (str): User's last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
