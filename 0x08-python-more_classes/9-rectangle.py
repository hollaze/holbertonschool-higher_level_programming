#!/usr/bin/python3
''' Rectangle class '''


class Rectangle:
    '''
    Class:
        defines a rectangle

        Class attributes:
                number_of_instances - increment during each new
                    instance instantiation;
                    decrement during each instance deletion
                print_symbol        - symbol for string representation

        Attributes:
                width   (int)
                height  (int)

        Methods:
                area        - give area of a rectangle
                perimeter   - give perimeter of a rectangle
                bigger_or_equal - returns biggest rectangle based on area
                square      - gives a square
                __str__     - prints character # in rectangle form
                __repr__    - prints string representation of the rectangle
                __del__     - prints Bye rectangle...
    '''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        s = ""
        for i in range(self.__height):
            for j in range(self.__width):
                s += str(self.print_symbol)
            if i < self.__height - 1:
                s += "\n"
        return s

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
