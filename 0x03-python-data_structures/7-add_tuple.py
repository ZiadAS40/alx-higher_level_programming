#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lenOfA = len(tuple_a)
    lenOfB = len(tuple_b)
    if lenOfA == 1:
        tuple_a = tuple_a[0], 0
    elif lenOfA == 0:
        tuple_a = 0, 0
    if lenOfB == 1:
        tuple_b = tuple_b[0], 0
    elif lenOfB == 0:
        tuple_b = 0, 0
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
