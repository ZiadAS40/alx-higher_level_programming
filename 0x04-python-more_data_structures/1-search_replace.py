#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def replacement(num):
        return replace if num == search else num
    return list(map(replacement, my_list))
