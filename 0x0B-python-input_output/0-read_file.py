#!/usr/bin/python3
def read_file(filename=""):
	"""
	This function reads the content of the given text file and prints it to stdout.

	>>> read_file("tests/sample_test.txt")
    Hello, this is a test file!

	"""
	with open(filename, 'r', encoding='utf-8') as file:
		content = file.read()
		print(content)

