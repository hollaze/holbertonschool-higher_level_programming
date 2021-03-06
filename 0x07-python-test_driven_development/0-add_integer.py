#!/usr/bin/python3
''' add_integer function '''


def add_integer(a, b=98):
    '''
    Add two integers

        Parameters:
                a (int)
                b (int)

        Returns:
                a + b
    '''

    if type(a) is float:
        a = int(a)
    elif type(a) is not int:
        raise TypeError("a must be an integer")

    if type(b) is float:
        b = int(b)
    elif type(b) is not int:
        raise TypeError("b must be an integer")

    return a + b
