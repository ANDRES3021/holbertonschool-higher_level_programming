#!/usr/bin/python3
"""Class Student"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return dictionary representation"""
        if attrs is None:
            return self.__dict__
        requested = {}
        for key_iterator in attrs:
            if key_iterator in self.__dict__.keys():
                requested[key_iterator] = self.__dict__[key_iterator]
        return requested

    def reload_from_json(self, json):
        """Reload the instance from a json"""
        if json != {}:
            self.first_name = json["first_name"]
            self.last_name = json["last_name"]
            self.age = json["age"]
