#!/usr/bin/python3
"""Base class"""


class Base:
    """the first class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialization of base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
