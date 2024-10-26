#!/usr/bin/python3
"""Rectangle class Representation"""


class Rectangle:
    """Class for printing dimensions of a rectangle.

    Takes in args for width and height of a rectangle, and contains methods
    for calculation of the area or perimeter.

    Attributes:
        number_of_instances (int): counter increment for every
            instantiation, and decrementing for every instance deletion.

    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Increments `number_of_instances` and calls setters for `__width`
        and `__height`.

        Args:
            width (int)
            height (int)

        """
        type(self).number_of_instances += 1
        # attribute assigment here engages setters defined below
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
        """Args:
            value (int)

        Attributes:
            __width (int)

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.

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
            ValueError: If `value` is less than 0.

        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Returns area of a rectangle.

        Attributes:
            __width (int)
            __height (int)

        Returns:
            Area of rectangle

        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a rectangle of given `width` and `height`

        Attributes:
            __width (int)
            __height (int)

        Returns:
            0 if either attribute is 0, or the perimeter

        """
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def _draw_rectangle(self):
        """Formats a string of '#' and '\n' chars to print the rectangle
        represented by the current instance.

        Attributes:
            __width (int)
            __height (int)
            str (str): string to be constructed

        Returns:
            str (str): string suitable for printing rectangle

        """
        str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                str += "{}".format(self.print_symbol)
            if self.__width != 0 and row < (self.__height - 1):
                str += '\n'
        return str

    def __str__(self):
        """Allows direct printing of instance.

        Returns:
            The output of _draw_rectangle, which creates a string
        representation of the rectangle.

        """
        return self._draw_rectangle()

    def __repr__(self):
        """Allows the use of eval().

        Returns:
            A string of the code to create the instance.

        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @classmethod
    def __del__(cls):
        """Decrements then prints message upon
        deletion of instance.

        """
        cls.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares the area and returns the larger of the two.

        Args:
            rect_1 (Rectangle object): first instance
            rect_2 (Rectangle object): second instance

        Raises:
            TypeError: if `rect_1` or `rect_2` is not an instance of Rectangle.

        Returns:
            `rect_1` if `rect_1` has alarger area than or equal to `rect_2`,
        or `rect_2` if it has the larger area

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

        @classmethod
    def square(cls, size=0):
        """Returns an instance with equal sides.

        Args:
            size(int)

        Returns:
            new instance of class with equal sides

        """
        return cls(size, size)
