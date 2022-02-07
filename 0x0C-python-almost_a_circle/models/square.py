#!/usr/bin/python3
"""square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialization of square class"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """size getter"""
        return self.height

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ public method that assigns an argument to each attribute"""
        if len(args) != 0:
            i = 1
            for arg in args:
                if i == 1:
                    self.id = arg
                elif i == 2:
                    self.size = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def __str__(self):
        """overriding the __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.height)
