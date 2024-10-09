#!/usr/bin/python3
"""define Rectangle class
"""


class Rectangle:
    """Rectangle class initiliazation

    Arguments:
        width (int): horizontal dimension of rectangle, defaults to 0
        height (int): vertical dimension of rectangle, defaults to 0

    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width getter.

        Returns:
            __width (int)

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Argsuments:
            value (int)

        Attributes:
            __width (int)

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than Zero.

        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """__height getter.

        Returns:
            __height (int)

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int)

        Attributes:
            __height (int)

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than Zero.

        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

     def area(self):
        """Returns area of a rectangle

        Attributes:
            __width (int)
            __height (int)

        Returns:
            Area of rectangle: __width * __height

        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a rectangle

        Attributes:
            __width (int)
            __height (int)

        Returns:
            0 if either attribute is 0, or the premiter if values are given

        """
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)
