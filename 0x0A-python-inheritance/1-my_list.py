#!/usr/bin/python3
"""Prints sorted list of attributes inherited from list class
"""
class MyList(list):
    """Print sorted list"""
    def print_sorted(self):
        print(sorted(self))
