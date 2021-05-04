#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_s = (len(sentence), sentence[0])
    if sentence == "":
        sentence[0] = None

    return tuple_s
