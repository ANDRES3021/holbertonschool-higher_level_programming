#!/usr/bin/python3
"""class keyword to define the class"""


class Square():
    """init method that receives the initialization parameters"""
    def __init__(self, size=0):
        """"I check ValueError and TypeError exceptions"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            """Expression to initialize our instance variable"""
            self.__size = size

    def area(self):
        return(self.__size**2)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def my_print(self):
        print("\n".join([''.join(["#" for y in range(self.__size)])
                         for x in range(self.__size)]))
