#!/usr/bin/python3
import sys
arg = sys.argv
result = 0
for n in range(1, len(arg)):
    result += int(arg[n])
print("{}".format(result))
