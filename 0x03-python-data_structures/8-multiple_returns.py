#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        firstChar = None
        lenOfSen = 0
    else:
        lenOfSen = len(sentence)
        firstChar = sentence[0]
    return (lenOfSen, firstChar)
