#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arg = sys.argv
    result = 0
    for n in range(1, len(arg)):
        result += int(arg[n])
    print("{}".format(result))
