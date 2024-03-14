#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    ls = list(dir(hidden_4))
    for n in ls:
        if not n.startswith('_'):
            print(n)
