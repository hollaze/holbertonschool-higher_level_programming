#!/usr/bin/python3
''' write_file function '''


def append_write(filename="", text=""):
    '''
    write in a file and appends in file
    '''
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
