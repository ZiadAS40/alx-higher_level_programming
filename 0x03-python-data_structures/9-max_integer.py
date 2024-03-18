#!/usr/bin/python3
def max_integer(my_list=[]):
    buffer = 0
    if len(my_list) == 0:
        return None
    for i in range(0 ,len(my_list)):
        if i + 1 == len(my_list):
            break
        if my_list[i] > my_list[i + 1] and my_list[i] > buffer:
            buffer = my_list[i]
        elif my_list[i] < my_list[i + 1] and my_list[i + 1] > buffer:
            buffer = my_list[i + 1]
    return buffer
