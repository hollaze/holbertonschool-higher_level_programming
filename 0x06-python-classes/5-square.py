#!/usr/bin/python3
""" Square class """


class Square:
    """
    Class:
        defines a square

    Attributes:
    -----------
    size : int
        size of the square
    position : tuple
        position of the square
    """

    def __init__(self, size=0):
        self.__size = size

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def position(self, value=0):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
