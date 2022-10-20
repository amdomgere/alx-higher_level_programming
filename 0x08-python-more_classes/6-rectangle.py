#!/usr/bin/python3
""" defines a class
"""


class Rectangle:
    """ class Rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Method that initializes instance
        Args:
        width, height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ method that returns the area """
        return self.width * self.height

    def perimeter(self):
        """method that returns the perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """ method that returns rectangle # """
        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """ method that returns the string """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ method to return Bye rectangle when an instance of
        rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
