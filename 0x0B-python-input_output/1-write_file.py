#!/usr/bin/python3
"""Module to know the length in a txt"""

def write_file(filename="", text=""):
    """this writes txt and return length"""
    with open(filename, mode="w", encoding="UTF8") as MyFile:
        return MyFile.write(text)
