#!/usr/bin/python3
"""Adds characters and returns length"""


def append_write(filename="", text=""):
    """Adds characters"""
    with open(filename, mode="a", encoding="UTF8") as MyFile:
        return MyFile.write(text)
