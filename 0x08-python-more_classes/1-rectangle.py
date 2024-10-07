#!/usr/bin/python3
class Rectangle:
    """ Rectangel class representaion
    """
    def __init(self, width=0, height=0):
        """ Rectangle class representaion """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter for the width attribute """
        return self.__width

    @width_setter
    def width(self, value):
        """ setter for the width attriubute """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter for the height attribute """
        return self.__height

    @height_setter
    def height(self, value):
        """ setter for the height attribute """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
