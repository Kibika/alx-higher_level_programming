#!/usr/bin/python3
"""
Square class uses getters and setters to check input
Raise Type error if input not integer
Raise value error if input is < 0
Calculates area if input correct
Prints Square to cmd
"""


class Square():
    """
    use setter to check input
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)
