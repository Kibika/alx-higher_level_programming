#!/usr/bin/python3
"""
Class rectangle that inherits from base
"""

from models.base import Base

class Rectangle(Base):
    """Class Rectangle"""
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize variables"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''
            Returning private attribute
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
            Setting private attribute
        '''
        self.setter_validation("width", value)
        self.__width = value

    @property
    def height(self):
        '''
            Returning private attribute
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
            Setting private attribute
        '''
        self.setter_validation("height", value)
        self.__height = value

    @property
    def x(self):
        '''
            Returning private attribute
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
            Setting private attribute
        '''
        self.setter_validation("x", value)
        self.__x = value

    @property
    def y(self):
        '''
            Returning private attribute
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
            Setting private attribute
        '''
        self.setter_validation("y", value)
        self.__y = value 

    @staticmethod
    def setter_validation(attribute, value):
        """checks for validity of input"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(attribute))
        if attribute == "x" or attribute == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(attribute))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    def area(self):
        """calculates area of rectangle"""
        area = self.width * self.height
        return area

    def display(self):
        '''
            Prints to stdout the representation of the rectangle
        '''
        rectangle = ""
        print("\n" * self.y, end="")
        for i in range(self.height):
            rectangle += (" " * self.x) + ("#" * self.width) + "\n"
        print(rectangle, end="")

    def __str__(self):
        '''
            Overwritting the str method
        '''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args):
        """Updates the arguments in the class"""
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass
