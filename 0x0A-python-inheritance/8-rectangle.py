#!/usr/bin/python3
"""task8"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """function that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that that validates value"""
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """class Rectangle"""
    def __init__(self, width, height):
        """initialize the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
