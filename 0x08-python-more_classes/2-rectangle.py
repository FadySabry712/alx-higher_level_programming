#!/usr/bin/python3
"""Defines a Rectangle"""


class Rectangle:
    """
    Class defines properties of rectangle.

    Attributes:
        width (int)
        height (int)
    """
    def __init__(self, width=0, height=0):
        """Creates new instances of Rectangle.

        Args:
            width (int, optional)
            height (int, optional)
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Width retriver.

        Returns:
            integer: the width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """Height retrive

        Returns:
            integer: the height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Property setter for width

        Args:
            value (int)

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than Zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Property setter for height

        Args:
            value (int)

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than Zero.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates the area

        Returns:
            integer: area.
        """
        return self.__height * self.__width

    def perimeter(self):
        """Calculates perimeter

        Returns:
            integer: perimeter.
        """
        if self.__height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)i
