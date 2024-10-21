#!/usr/bin/python3
""" REctangle class that extends Base class """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class instance of Base class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ class constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ rectangle width """
        return self.__width

    @width.setter
    def width(self, Value):
        self.validate_integer("width", value, False)
        self.__width = Value

    @property
    def heigt(self):
        """ rectangle height """
        return self.__height

    @height.setter
    def height(self, Value):
        self.validate_integer("height", value, False)
        self.__height = Value

    @property
    def x(self):
        """ rectangle x value """
        return self.__x

    @x.setter
    def x(self, Value):
        self.validate_integer("x", value)
        self.__x = Value

    @property
    def y(self):
        """ rectangle y Value """
        return self.__y

    @y.setter
    def y(self, Value):
        self.validate_integer("y", value)
        self.__y = Value

    def validate_integer(self, name, value, eq=True);
        """ method for validating values and integers """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """ return area of a rectangle """
        return self.width * self.height

    def display(self):
        """ print hastage representation of the rectangle """
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')

    def __str__(self):
        """Returns string information about this rectangle"""
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """updates instance attributes via */**args."""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Updates instance attributes with no-keyword & keyword inputs"""
        # print(args, kwargs)
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)
