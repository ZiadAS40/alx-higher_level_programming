#!/usr/bin/python3
def fizzbuzz():
    arr = list(range(1, 101))
    for n in arr:
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz ", end='')
        elif n % 3 == 0:
            print("Fizz ", end='')
        elif n % 5 == 0:
            print("Buzz ", end='')
        else:
            print(n, end=' ')
    print()
