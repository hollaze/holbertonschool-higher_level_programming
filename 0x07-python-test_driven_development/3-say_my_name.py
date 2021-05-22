#!/usr/bin/python3
''' say_my_name function '''


def say_my_name(first_name, last_name=""):
    '''
    Print first and last name

        Parameters:
                first_name  (str)
                last_name   (str)

        Returns:
                void
    '''
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
