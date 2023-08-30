#!/usr/bin/python3
"""Defines a class Square"""

class Square:
	 """
	A class that defines a square with a private attribute size and validation

	Attributes:
		size: size of a square
	"""
	def __init__(self, size=0):
		 """Creates new instances of square.

		Args:
			size: size of the square
		"""
		self.__size = size

		if not isinstance(size, int):
			raise TypeError("size must be an integer")
		elif size < 0:
			raise ValueError("size must be >= 0")
		 else:
			self.__size = size
