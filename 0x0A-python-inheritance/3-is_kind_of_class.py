#!/usr/bin/python3
''' kind of class'''


def is_kind_of_class(obj, a_class):
    '''
    same class inherit from
    '''
    if isinstance(obj, a_class):
        return True
    return False
