#!/usr/bin/python3
"""
    Define File Storage module
"""
import json
import datetime


class FileStorage:
    """ Serializes instances to a JSON file
        and deserializes JSON file to instances
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """  sets in __objects the obj with key <obj class name>.id """
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path). """
        mydict = {}

        for key, value in FileStorage.__objects.items():
            mydict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as myFile:
            json.dump(mydict, myFile)

    def reload(self):
        """ deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
