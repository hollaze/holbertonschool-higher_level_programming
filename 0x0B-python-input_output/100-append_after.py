#!/usr/bin/python3
""" inserts lines of text to a file """


def append_after(filename="", search_string="", new_string=""):
    """ inserts lines of text to a file """
    text = ""
    with open(filename, 'r') as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, 'w') as file:
        file.write(text)
