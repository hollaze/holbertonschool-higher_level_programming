#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as exception:
        print("Exception:", exception, file=sys.stderr)
        return None
