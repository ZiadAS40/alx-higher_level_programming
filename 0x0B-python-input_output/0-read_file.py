#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as file:
        result = file.read()
        print(result)
