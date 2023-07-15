#!/usr/bin/python3
"""
Module: review

This module defines the Review class, which inherits from
BaseModel and represents a review.

Classes:
    Review: A class that represents a review with place_id,
    user_id, and text attributes.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel and represents a review.

    Public Class Attributes:
        place_id (str): ID of the place associated with the review.
        user_id (str): ID of the user associated with the review.
        text (str): Text content of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
