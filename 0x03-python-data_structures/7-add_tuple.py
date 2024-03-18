#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = 0
    b = 0
    lenOfA = len(tuple_a)
    lenOfB = len(tuple_b)
    if lenOfA == 1:
        a += tuple_a[0]
    elif lenOfA == 2:
        a += tuple_a[0]
        b += tuple_a[1]
    else:
        a += 0
        b += 0
    if lenOfB == 1:
        a += tuple_b[0]
    elif lenOfB == 2:
        a += tuple_b[0]
        b += tuple_b[1]
    else:
        a += 0
        b += 0
    new_tuple = a, b
    return new_tuple
