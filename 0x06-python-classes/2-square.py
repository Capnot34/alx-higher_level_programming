#!/usr/bin/python3
"""Define a class Square."""


class Square:
	"""A class that defines a square with a private attribute size and validations
	"""

	def __init__(self, size=0):
	"""Initialize the square with a size with validation
	"""
	if not isinstance(size, int):
		 raise TypeError("size must be an integer")
	if size < 0:
		 raise ValueError("size must be >= 0")
	self.__size = size
