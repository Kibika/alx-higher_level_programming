#!/usr/bin/python3
"""Function that appends to text file
"""


def append_write(filename="", text=""):
    """append module"""
    with open(filename, "a", encoding="utf-8") as f:
       return f.write(text)
