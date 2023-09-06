#!/usr/bin/python3
"""
Module 3-rectangle
Defines a Rectangle.
"""

class Rectangle:
    """Represents a Rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__width + 2 * self.__height

    def __str__(self):
        """String representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
    
        rectangle_str = []
        for _ in range(self.__height):
            rectangle_str.append("#" * self.__width)
    
        return "\n".join(rectangle_str)

    def __repr__(self):
        """Official string representation."""
        return "Rectangle({}, {})".format(self.__width, self.__height)
