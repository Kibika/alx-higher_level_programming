#!/usr/bin/python3
"""Inherit from rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Area of a square"""
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
    """Print Format"""
    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
