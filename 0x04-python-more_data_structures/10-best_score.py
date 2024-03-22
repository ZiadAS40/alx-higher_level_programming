#!/usr/bin/python3
def best_score(a_dictionary):
    score = 0
    if a_dictionary is not None:
        for v in sorted(a_dictionary):
            if a_dictionary[v] > score:
                score = a_dictionary[v]
                theBest = v
        return theBest
    else:
        return None
