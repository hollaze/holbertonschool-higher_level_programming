#!/usr/bin/python3
''' Rectangle class '''

class Rectangle:
    '''
    Class:
        defines a rectangle,
        calulate Area and perimeter,
        get rectangle into #

        Returns:
                width       (int)
                height      (int)
                area        (def)
                perimeter   (def)
                s           (string)
    '''

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h_value):
        if type(h_value) is not int:
            raise TypeError("height must be an integer")
        if h_value < 0:
            raise ValueError("height must be >= 0")
        self.__height = h_value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w_value):
        if type(w_value) is not int:
            raise TypeError("width must be an integer")
        if w_value < 0:
            raise ValueError("width must be >= 0")
        self.__width = w_value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        s = ""
        for i in range(self.height):
            for j in range(self.width):
                s += "#"
            if i < self.height - 1:
                s += "\n"
        return s

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
