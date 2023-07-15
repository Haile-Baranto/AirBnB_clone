#!/usr/bin/python3
"""
Module: amenity

This module defines the Amenity class, which inherits
from BaseModel and represents an amenity.

Classes:
    Amenity: A class that represents an amenity with
    public class attributes.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel and represents an amenity.

    Public Class Attributes:
        name (str): Name of the amenity.
    """

    name = ""
