#!/usr/bin/python3
""" Write student class """


class Student:
    def __init__(self, first_name, last_name, age):
        """ instantiation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ class to dict """
        return self.__dict__
