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

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__position[1]):
            print()
        for row in range(self.__size):
            print("{}{}".format(" " * self.__position[0], "#" * self.__size))

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2 \
                and isinstance(value[0], int) and isinstance(value[1], int) \
                and value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
