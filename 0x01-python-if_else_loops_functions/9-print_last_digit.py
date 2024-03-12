#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        ncpy = number * -1
        return (ncpy % 10) * -1
    else:
        return number % 10
