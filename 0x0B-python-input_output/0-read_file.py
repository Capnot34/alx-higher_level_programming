#!/usr/bin/python3

def read_file(filename=""):
	"""
	Read the content of a file and print it to stdout.

	Args:
		filename (str): The path to the file to be read. Defaults to an empty string.
	Returns:
		None: This function doesn't return anything; it prints the file's content.
	Raises:
		FileNotFoundError: If the provided filename does not exist.
	
	Example:
		>>> read_file("tests/sample_test.txt")
		Hello, this is a test file!

	"""
	with open(filename, 'r', encoding='utf-8') as file:
		content = file.read()
		print(content, end='')
