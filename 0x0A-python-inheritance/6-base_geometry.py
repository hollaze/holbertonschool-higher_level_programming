#!/usr/bin/python3
''' BaseGemetry class '''


class BaseGeometry:
    '''
    raise exception if area is not implemented
    '''

    def area(self):
        raise Exception("area() is not implemented")
