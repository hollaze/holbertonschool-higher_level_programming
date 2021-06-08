#!/usr/bin/python3
""" Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines a Square
        Inherited from Rectangle

    Args:
        Rectangle (class): Defines a Rectangle

    Methods:
        __str__
        validate_int
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        gives informations of a square

        Returns:
            [str]: informations
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)

    def validate_int(self, name, number):
        """
        check if a number is an int

        Parameters:
            self    (Rectangle)
            name    (str)
            number  (int)
        """
        if type(number) is not int:
            raise TypeError("{} must be an integer".format(name))

    """ getter setter """
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.validate_int("width", value)
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
