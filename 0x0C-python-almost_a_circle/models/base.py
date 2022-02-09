#!/usr/bin/python3
"""This is the Base module.
Contains the Base class which will be the
“base” of all other classes in this project.
"""
import json
import csv


class Base():
    """This class will be the “base” of all other classes in this project.
        The goal is to manage id attribute in all our future classes
        and to avoid duplicating the same code and same errors.
        Attributes:
        __nb_objects (int): the number of created Base objects.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the default attributes of the Base object.
        Args:
            id (int): the identifier of the Base object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += +1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.
        Args:
            list_dictionaries (list): a list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.
        Args:
            list_objs (list): a list of objects.
        """
        lst = []
        if list_objs is not None and len(list_objs) > 0:
            for obj in list_objs:
                lst.append(obj.to_dictionary())
        with open(cls.__name__ + ".json", 'w') as f:
            f.write(Base.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.
        Args:
            json_string (str): string representing a list of dictionaries.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.
        Args:
            dictionary (dict): the values of the wanted instance.
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        try:
            with open(cls.__name__ + ".json", "r") as My_file:
                read_file = My_file.read()
                list_dicci = cls.from_json_string(read_file)
                lists_1 = []
                for lis in list_dicci:
                    lists_1.append(cls.create(**lis))
                return lists_1
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """create file .csv"""
        line = []
        with open(cls.__name__ + ".csv", "w") as my_file:
            if list_objs is None or len(list_objs) <= 0:
                my_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    line = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    line = ["id", "size", "x", "y"]
            var = csv.DictWriter(my_file, fieldnames=line)
            for iter in list_objs:
                var.writerow(iter.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """read the function"""
        try:
            with open(cls.__name__ + ".csv", "r") as my_file:
                if cls.__name__ == "Rectangle":
                    line = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    line = ["id", "size", "x", "y"]
                read_file = csv.DictReader(my_file, fieldnames=line)
                dict_ni = [
                    dict([clave, int(valor)] for clave, valor in iter.items())
                    for iter in read_file
                ]
                return [cls.create(**dict_l) for dict_l in dict_ni]
        except Exception:
            return []
