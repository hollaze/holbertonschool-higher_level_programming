#!/usr/bin/python3
''' BaseGeometry class '''


class BaseGeometry:
    '''
    raise exception if area is not implemented
    validates value
    '''

    def area(self):
        ''' area function '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' integer validator function'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


''' Rectangle class '''


class Rectangle(BaseGeometry):
    '''
    Subclass of BaseGeometry
    '''

    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
