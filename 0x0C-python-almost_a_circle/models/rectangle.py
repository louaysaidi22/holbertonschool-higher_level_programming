#!/usr/bin/python3
"""rectangle class"""
from cmath import atan
from models.base import Base


class Rectangle(Base):
    """Class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization of rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """public method that returns the area value of the Rectangle"""
        return self.width * self.height

    def display(self):
        """ public method that prints in stdout
        the Rectangle instance with the character #"""
        if self.width == 0 or self.height == 0:
            print("")
        else:
            for p in range(self.y):
                print("")
            for i in range(self.height):
                for k in range(self.x):
                    print(" ", end="")
                for j in range(self.width):
                    print("#", end="")
                print("")

    def update(self, *args, **kwargs):
        """ public method that assigns an argument to each attribute"""
        if len(args) != 0:
            i = 1
            for arg in args:
                if i == 1:
                    self.id = arg
                elif i == 2:
                    self.width = arg
                elif i == 3:
                    self.height = arg
                elif i == 4:
                    self.x = arg
                elif i == 5:
                    self.y = arg
                i += 1
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        dic = {
            "id": self.id,
            "width": self.width,
            "hgeight": self.height,
            "x": self.x,
            "y": self.y
        }
        return dic

    def __str__(self):
        """overriding the __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)
