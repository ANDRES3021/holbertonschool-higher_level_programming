#!/usr/bin/python3
"""Module Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class BaseGeometry"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Find the Area"""
        return self.__width * self.__height

    def __str__(self):
        """Overcharge __str__"""
        string = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return string
