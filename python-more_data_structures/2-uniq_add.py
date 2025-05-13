#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = 0
    integer = set(my_list)
    for i in integer:
        result += i
    return result
