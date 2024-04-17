#!/usr/bin/python3
"""
isert a line after a certain string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    a function that inserts a line of text to a file, after each line containing a specific string 
    """
    with open(filename, 'r', encoding='utf-8') as f:
        myList = []
        while True:
            myLine = f.readline()
            if myLine == "":
                break
            myList.append(myLine)
            if search_string in myLine:
                myList.append(new_string)
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(myList)
