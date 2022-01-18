#!/usr/bin/python3
"""task 4"""


class Square:
    """a class Square that defines a square"""

    def __init__(self, size=0):
        """initialisation"""
        self.__size = size

    @property
    def size(self):
        """get the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area"""
        return self.__size ** 2
