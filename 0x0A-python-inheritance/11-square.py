#!/usr/bin/python3
'''Module for 10-Rectangle class.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A subclass representtion of a rectangle.'''
    def __init__(self, size):
        '''Constructor.'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Method for area'''
        return self.__size ** 2

    def __str__(self):
        ''' return string repr of the square '''
        return "[Square] " + str(self.__size) + "/" str(self.__size)
