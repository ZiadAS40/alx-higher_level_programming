#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dlist = sorted(a_dictionary)
    for i in dlist:
        print("{}: {}".format(i, a_dictionary[i]))
