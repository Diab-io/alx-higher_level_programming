#!/usr/bin/python3
""" A class that inherits from rectangle class """

from models.rectangle import Rectangle

class Square(Rectangle):
    """ Represents a square """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializing square class"""
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        """ Printing square class by overloading __str__ method """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ Getting size of square """
        return self.__width
    
    @size.setter
    def size(self, value):
        """ setting size of square """
        self.__width = value
        self.__height = value