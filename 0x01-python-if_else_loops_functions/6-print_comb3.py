#!/usr/bin/python3
list = list(range(0, 10))
for i in range(0, 10):
    for j in list:
        if (i != j):
            if (i != 9) and (i != 8):
                print("{}{}, ".format(i, j), end='')
    list.pop(0)
print("89")
