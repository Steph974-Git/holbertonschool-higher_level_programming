#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_a_dict = {}
    for key in a_dictionary:
        new_a_dict[key] = a_dictionary[key] * 2
    return new_a_dict
