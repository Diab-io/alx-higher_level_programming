#!/usr/bin/python3
""" A class that inherits from base class """

from base import Base

class Rectangle(Base):
    """ Represents a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initialize a new rectangle

            Args:
                width(int): The width of the new rectangle
                height(int): The height of the new rectangle
                x(int): The x-coordinates of the rectangle
                y(int): The y-coordinates of the rectangle
                id(int): The id of the new rectangle
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y 
        super().__init__(id)
    
    @property
    def width(self):
        """ set/get the width of the rectangle"""
        return self.__width
    
    @width.setter
    def width(self, value):
        self.__width = value
    
    @property
    def height(self):
        """ set/get the height of the rectangle"""
        return self.__height
    
    @height.setter
    def height(self, value):
        self.__height = value
    
    @property
    def get_x(self):
        """ set/get the x coordinate of the rectangle"""
        return self.__x
    
    @get_x.setter
    def get_x(self, value):
        self.__x = value

    @property
    def get_y(self):
        """ set/get the y coordinate of the rectangle"""
        return self.__y
    
    @get_y.setter
    def get_y(self, value):
        self.__y = value