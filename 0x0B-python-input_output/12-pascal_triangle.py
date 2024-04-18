#!/usr/bin/python3
def pascal_triangle(n):
    if n > 1:
        t_list = [1]
    else:
        return []
    result_list = []
    for n in range(n):
        result_list.append(t_list)
        t_list.append(0)
        t_list.insert(0, 0)
        eTempList = [t_list[i] + t_list[i + 1] for i in range(len(t_list) - 1)]
        t_list.pop()
        t_list.pop(0)
        t_list = eTempList
    return result_list
