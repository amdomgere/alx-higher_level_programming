#!/usr/bin/python3
""" defines a class
"""


class Rectangle:
    """ class Rectangle"""
    def __init__(self, width=0, height=0):
        """ Method that initializes instance
        Args:
        width, height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ method that returns height """
        return self.__width

    @width.setter
    def width(self, value):
        """ method that defines width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ method that defines height"""
        return self.__height

    @height.setter
    def height(self, value):
        """method that defines height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
