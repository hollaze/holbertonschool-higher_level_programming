#!/usr/bin/python3
''' from json string function '''
import json


def from_json_string(my_str):
    '''
    from string to dict
    '''
    return json.loads(my_str)
