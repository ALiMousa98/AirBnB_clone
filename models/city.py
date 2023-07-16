#!/usr/bin/python3
"""This module creates a City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """This is the class for managing user objects"""

    name = ""
    state_id = ""

    def to_dict(self):
        """ a dictionary representation for BaseModel Class """
        obj_dict = dict(self.__dict__)
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()
        obj_dict['name'] = name
        obj_dict['state_id'] = state_id

        return obj_dict
