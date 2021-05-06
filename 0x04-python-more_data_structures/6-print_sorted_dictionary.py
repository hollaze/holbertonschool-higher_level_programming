#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
        for i in list(sorted(a_dictionary)):
            '#i is key and a_dictionary[i] is like: [i] is element of i'
            '#So [values] is element of key'
            print(i, a_dictionary[i], sep=": ")
