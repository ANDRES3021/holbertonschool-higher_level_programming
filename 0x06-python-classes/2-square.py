#!/usr/bin/python3
"""class keyword to define the class"""


class Square():
    """init method that receives the initialization parameters"""
    def __init__(self, size=0):
        """"I check ValueError and TypeError exceptions"""
        if  isinstance(size, int) == False:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            """Expression to initialize our instance variable"""
            self.__size = size
