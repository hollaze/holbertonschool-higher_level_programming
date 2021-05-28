#!/usr/bin/python3
''' text indentation function '''

def text_indentation(text):
    '''
    indent every time there is a ',' , ':' , '?'
    prints a new line
    
        Parameter:
                text    (str)
                
        Returns:
                void
    '''
    i = 0

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    while i < len(text):
        print(text[i], end='')
        if text[i] in ['.', ':', '?']:
            print('\n')
            if text[i + 1] is ' ':
                i += 1
        i += 1
    print('\n')
