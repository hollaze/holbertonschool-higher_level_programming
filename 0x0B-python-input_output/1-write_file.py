#!/usr/bin/python3
''' write_file function '''


def write_file(filename="", text=""):
    '''
    write in a file
    '''
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
