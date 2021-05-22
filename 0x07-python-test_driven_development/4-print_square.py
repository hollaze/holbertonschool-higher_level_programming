#!/usr/bin/python3
''' print_square function '''


def print_square(size):
    '''
    Prints a square with #

        Parameter:
                size (int)

        Returns:
                void
    '''

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
