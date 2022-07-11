#!/usr/bin/python3
"""Read file and print to standard output
"""
def read_file(filename=""):
    """Read file module"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
