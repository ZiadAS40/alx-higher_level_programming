#!/usr/bin/python3
def multiple_returns(sentence):
    lenOfSen = len(sentence)
    firstChar = sentence[0]
    if sentence == "":
        firstChar = None
    return (lenOfSen, firstChar)
