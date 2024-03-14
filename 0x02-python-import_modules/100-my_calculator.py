#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    arg = sys.argv
    if len(arg) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(arg[1])
        b = int(arg[3])
        if arg[2] == '+':
            print(add(a, b))
        elif arg[2] == '-':
            print(sub(a, b))
        elif arg[2] == '*':
            print(mul(a, b))
        elif arg[2] == '/':
            print(div(a, b))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
