#!/usr/bin/python3
letters = list(range(97, 122))
ascii_char = [chr(letter) for letter in letters]
print(''.join(ascii_char), end='')
