#!/usr/bin/python3


def text_indentation(text):

    i = 0

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    while i < len(text):
        print(text[i], end='')
        if text[i] in ['.', ':', '?']:
            print('\n')
        i += 1
    print('\n')
