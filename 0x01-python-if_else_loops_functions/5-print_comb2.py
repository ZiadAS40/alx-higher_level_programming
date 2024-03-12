#!/usr/bin/python3
numbers = list(range(0, 99))
for number in numbers:
    print("{:02d},".format(number), end=' ')
print("99")
