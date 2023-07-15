#!/usr/bin/python3
"""
    this is the base model to be inheirted by all classes
    Parent Class
"""

# imports
import uuid
from datetime import datetime


class BaseModel:
    """
        Defines all common attributes and methods for other classes
        Also links BaseModel to FileStorage by using the variable storage
    """
    def __init__(self):
        """ initialize the BaseModel instance
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """String representation of a BaseModel instance"""
        return ("[{}] ({}) {} "
                .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ update (updated_at) var with current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ a dictionary representation for BaseModel Class """
        obj_dict = dict(self.__dict__)
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()

        return obj_dict
