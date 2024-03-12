#!/usr/bin/python3
letters = list(range(97, 123))
for letter in letters:
    if (chr(letter) != 'q') and (chr(letter) != 'e'):
        print("{}".format(chr(letter)), end='')
