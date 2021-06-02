#!/usr/bin/python3
''' add attribute function '''


def add_attribute(obj, name, value):
    ''' add attribute to a class '''
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    return setattr(obj, name, value)
