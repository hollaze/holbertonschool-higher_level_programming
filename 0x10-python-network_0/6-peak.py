#!/usr/bin/python3
"""Find a peak"""


def find_peak(list_of_integers):
    """Function to find a peak"""

    if len(list_of_integers) <= 0:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
