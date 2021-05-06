#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        [print(i) for i in list(sorted(a_dictionary.items()))]
