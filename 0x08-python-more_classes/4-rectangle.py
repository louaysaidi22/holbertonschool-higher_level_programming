#!/usr/bin/python3
"""task 4"""


class Rectangle:
    """a class Rectangle that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """initialisation"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the heigth"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """print the rectangle with the character #"""
        str = ""
        if self.__width == 0 or self.__height == 0:
            return str
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    str += "#"
                if i != self.__height - 1:
                    str += "\n"
            return str

    def __repr__(self):
        """return a string representation of the rectangle"""
        s = "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
        return s
