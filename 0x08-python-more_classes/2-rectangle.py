#!/usr/bin/python3


class Rectangle:
    '''
    Class:
        defines a rectangle,
        calulate Area and perimeter

        Returns:
                width       (int)
                height      (int)
                area        (def)
                perimeter   (def)
    '''

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h_value):
        if type(self.__height) is not int:
            raise TypeError("height must be an integer")
        if self.height < 0:
            raise ValueError("height must be >= 0")
        self.__height = h_value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w_value):
        if type(self.__width) is not int:
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = w_value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
