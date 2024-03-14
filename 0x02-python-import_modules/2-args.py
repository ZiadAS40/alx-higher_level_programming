#!/usr/bin/python3
import sys
arg = sys.argv
if __name__ == "__main__":
    nls = len(arg)
    print("{} {}{}".format(nls - 1, "argument" if nls - 1 == 1 else "arguments", ':' if nls > 1 else '.'))
    for n in range(1, nls):
        print("{}: {}".format(n, arg[n]))
