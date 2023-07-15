#!/usr/bin/python3
"""
Module: city

This module defines the City class, which inherits from
BaseModel and represents a city.

Classes:
    City: A class that represents a city with state_id and
    name attributes.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel and represents a city.

    Public Class Attributes:
        state_id (str): ID of the state associated with the city.
        name (str): Name of the city.
    """

    state_id = ""
    name = ""
