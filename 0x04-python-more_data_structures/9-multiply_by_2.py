#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()

    for values in new_dic:
        new_dic[values] *= 2

    return new_dic
