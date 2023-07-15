#!/usr/bin/python3
import uuid
from datetime import datetime
import models
"""
Module: base_model

This module defines the BaseModel class, which serves as a base model for
other classes.

Classes:
    BaseModel: A base model that defines common attributes and methods for
    other classes.
"""


class BaseModel:
    """
    A base model that defines common attributes and methods for other classes.

    Attributes:
        id (str): Unique identifier for the instance (generated using
        uuid.uuid4()).
        created_at (datetime.datetime): The timestamp of when the instance was
        created.
        updated_at (datetime.datetime): The timestamp of the last update to
        the instance.

    Methods:
        __init__(): Initialize a new instance of the BaseModel class.
        __str__(): Return a string representation of the BaseModel instance.
        save(): Update the updated_at attribute with the current datetime.
        to_dict(): Return a dictionary representation of the BaseModel
        instance.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of the BaseModel class.

        If kwargs is not empty, create attributes from the dictionary
        representation. Otherwise, generate a new id using uuid.uuid4().
        Set the created_at and updated_at attributes to the current datetime.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments. Each key represents an
            attribute name and each value represents the corresponding
            attribute value.

        Note:
            - The '__class__' key is not added as an attribute.
            - The 'created_at' and 'updated_at' attributes should be in string
            format, which can be converted back to datetime objects using the
            format '%Y-%m-%dT%H:%M:%S.%f'.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key,
                                datetime.strptime(value,
                                                  '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
            models.storage.new(self)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return a string representation of the BaseModel instance.

        Returns:
            str: String representation of the instance, including class name,
            id, and attribute dictionary.
        """

        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Update the updated_at attribute with the current datetime.
        This method will be called whenever there is an update to
        the instance.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary representation of the BaseModel instance.

        Returns:
            dict: Dictionary representation of the instance, including class
            name and attribute values.
        """

        d = self.__dict__.copy()
        d['__class__'] = type(self).__name__
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        return d
