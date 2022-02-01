#!/usr/bin/python3
"""Module 0"""


def read_file(filename=""):
    """Read a file"""
    with open(filename, mode="r", encoding="UTF8") as MyFile:
        print(MyFile.read(), end="")
