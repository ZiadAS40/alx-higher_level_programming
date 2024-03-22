#!/usr/bin/python3
def roman_to_int(roman_string):
    rA = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    skip_next = False
    for i in range(0, len(roman_string)):
        if skip_next == True:
            skip_next = False
            continue
        if i != len(roman_string) - 1:
            if rA[roman_string[i]] < rA[roman_string[i + 1]]:
                result += rA[roman_string[i + 1]] - rA[roman_string[i]]
                skip_next = True
            else:
                result += rA[roman_string[i]]
                skip_next = False
        else:
            result += rA[roman_string[i]]
    return result
