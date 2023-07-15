#!/usr/bin/python3
"""
    this is the base model to be inheirted by all classes
    Parent Class
"""

# imports
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
        Defines all common attributes and methods for other classes
        Also links BaseModel to FileStorage by using the variable storage
    """
    def __init__(self, *args, **kwargs):
        """ initialize the BaseModel instance

            Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """
        if kwargs:
            kwargs.pop('__class__', None)
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """String representation of a BaseModel instance"""
        return ("[{}] ({}) {} "
                .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ update (updated_at) var with current datetime """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ a dictionary representation for BaseModel Class """
        obj_dict = dict(self.__dict__)
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()

        return obj_dict
