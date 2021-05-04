#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_s = (len(sentence), sentence[0])
    if not sentence:
        return (0, None)

    return tuple_s
