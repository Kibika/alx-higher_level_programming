#!/usr/bin/python3
"""Write string to text file
"""


def write_file(filename="", text=""):
    """write to file module"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
