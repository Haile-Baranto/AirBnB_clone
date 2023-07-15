#!/usr/bin/python3
"""
Module: place

This module defines the Place class, which inherits from
BaseModel and represents a place.

Classes:
    Place: A class that represents a place with city_id, user_id,
    name, description, number of rooms, number of bathrooms, maximum
    guest capacity, price per night, latitude, longitude, and a list
    of amenity ids attributes.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class that inherits from BaseModel and represents a place.

    Public Class Attributes:
        city_id (str): ID of the city associated with the place.
        user_id (str): ID of the user associated with the place.
        name (str): Name of the place.
        description (str): Description of the place.
        number_rooms (int): Number of rooms in the place.
        number_bathrooms (int): Number of bathrooms in the place.
        max_guest (int): Maximum guest capacity of the place.
        price_by_night (int): Price per night for the place.
        latitude (float): Latitude coordinate of the place.
        longitude (float): Longitude coordinate of the place.
        amenity_ids (list): List of amenity IDs associated with the place.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
