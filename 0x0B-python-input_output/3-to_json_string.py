#!/usr/bin/python3
''' json string function '''
import json


def to_json_string(my_obj):
    '''
    from dict to string
    '''
    return json.dumps(my_obj)
