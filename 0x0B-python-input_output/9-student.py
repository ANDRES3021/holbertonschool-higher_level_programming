#!/usr/bin/python3
"""Class Student"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self):
            """return dictionary representation"""
            return self.__dict__
