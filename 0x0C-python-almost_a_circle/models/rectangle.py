#!/usr/bin/python3
''' Rectangle class '''
from models.base import Base


class Rectangle(Base):
    """
    Set a Rectangle

    Args:
        Base (inherited class): Base for all clases

    Methods:
        validate_int
        area
        display
        update
        __str__
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

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

    def area(self):
        """
        gives area of a retangle

        Parameter:
            self    (Rectangle)

        Returns:
            area of the rectangle
        """
        return self.__height * self.__width

    def display(self):
        """
        display a rectangle in stdout

        Parameter:
            self    (Rectangle)
        """
        print("\n" * self.__y, end='')
        for row in range(self.__height):
            if self.__x:
                print(" " * (self.__x - 1), end='')
            if self.__width:
                print("#" * self.__width)

    def update(self, *args, **kwargs):
        """
        update arguments

        Parameters:
            self    (Rectangle)
            args    (Any)
            kwargs  (dict)
        """
        if args and args is not None:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def __str__(self):
        """
        gives information about the Rectangle

        Parameter:
            self    (Rectangle)

        Returns:
            s:      informations
        """
        s = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                    self.x, self.y,
                                                    self.width, self.height)
        return s

    """ height getter - setter """
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_int("height", value)
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    """ width getter - setter """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_int("width", value)
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    """ x getter - setter """
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_int("x", value)
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    """ y getter - setter """
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_int("y", value)
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
