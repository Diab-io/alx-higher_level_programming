#!/usr/bin/python3
""" A class that inherits from base class """

from models.base import Base

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
            Raises:
                TypeError: If either of width or height is not an int.
                ValueError: If either of width or height <= 0.
                TypeError: If either of x or y is not an int.
                ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y 
        super().__init__(id)
    
    @property
    def width(self):
        """ set/get the width of the rectangle"""
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value
    
    @property
    def height(self):
        """ set/get the height of the rectangle"""
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value
    
    @property
    def x(self):
        """ set/get the x coordinate of the rectangle"""
        return self.__x
    
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """ set/get the y coordinate of the rectangle"""
        return self.__y
    
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be > 0")
        self.__y = value
    
    def area(self):
        """ returns area of the rectangle """
        return self.width * self.height
    
    def display(self):
        """ prints out the rectangle """
        [print("") for i in range(self.y)]
        for i in range(self.height):
            print(" "*self.x + "#"*self.width)
    
    def update(self, *args):
        """Update the Rectangle.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

    def __str__(self):
        """ overriding the str method """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)