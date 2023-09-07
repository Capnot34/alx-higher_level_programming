#!/usr/bin/python3
"""
Module 7-rectangle
Defines a Rectangle.
"""


class Rectangle:
    """Represents a Rectangle."""

    number_of_instances = 0
    # Class attribute to keep track of the number of instances
    print_symbol = "#"
    # Class attribute to define the symbol for string representation

    def __init__(self, width=0, height=0):
        """Initializes the rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment the number of instances

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
        """String representation of the rectangle using the print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = []
        for _ in range(self.__height):
            rectangle_str.append(str(self.print_symbol) * self.__width)

        return "\n".join(rectangle_str)

    def __repr__(self):
        """Official string representation."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message when the rectangle
        is deleted and decrements the number of instances.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1  # Decrement the number of instances
