#!/usr/bin/python3
''' Square class inherits Rectangle '''
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''
    defines a square with inheritance
    '''
    
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
