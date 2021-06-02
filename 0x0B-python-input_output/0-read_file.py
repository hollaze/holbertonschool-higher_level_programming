#!/usr/bin/python3
''' read_file function '''


def read_file(filename=""):
    '''
    reads a file
    '''
    with open(filename) as file:
        print(file.read())
