#!/usr/bin/python3
""" Write student class """


class Student:
    def __init__(self, first_name, last_name, age):
        """ instantiation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ class to dict """
        dico = {}

        if attrs is None:
            return self.__dict__

        for i in attrs:
            if type(i) is str and hasattr(self, i):
                dico[i] = getattr(self, i)
        return dico
