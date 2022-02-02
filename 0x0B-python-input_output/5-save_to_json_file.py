#!/usr/bin/python3
"""Module writes an Object to a text file,
using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """ Function that writes an Object to a text file, using a JSON"""
    with open(filename, mode="w", encoding="UTF8") as MyFile:
        MyFile.write(json.dumps(my_obj))
