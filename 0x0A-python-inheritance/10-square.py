#!/usr/bin/python3
"""Square Class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """instantiate size and implement area"""
    def __init__(self, size):
        super().__init__(size, size)
