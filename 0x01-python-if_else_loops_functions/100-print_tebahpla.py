#!/usr/bin/python3
for n in range(ord('z'), ord('a') - 1, -1):
    if n % 2 != 0:
        print("{:c}".format(n - 32), end='')
    else:
        print("{:c}".format(n), end='')
