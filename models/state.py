#!/usr/bin/python3
"""
Module: state

This module defines the State class, which inherits from
BaseModel and represents a state.

Classes:
    State: A class that represents a state with a name attribute.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that inherits from BaseModel and represents a state.

    Public Class Attributes:
        name (str): Name of the state.
    """

    name = ""
