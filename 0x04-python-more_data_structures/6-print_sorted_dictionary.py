#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
        for i in list(sorted(a_dictionary)):
            '#i is key'
            print(i, a_dictionary[i], sep=": ")
