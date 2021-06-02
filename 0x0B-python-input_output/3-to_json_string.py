#!/usr/bin/python3
''' json string function '''
import json


def to_json_string(my_obj):
    '''
    return JSON reprensentation of an object
    '''
    return json.dumps(my_obj)
