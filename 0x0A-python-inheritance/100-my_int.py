#!/usr/bin/python3
''' int subclass '''


class MyInt(int):
    '''
    invert True and False for == and !=
    '''

    def __eq__(self, other):
        return super() == other

    def __ne__(self, other):
        return not self.__eq__(other)
