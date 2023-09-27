#!/usr/bin/python3
"""
This module provides a function to indent a given text after certain punctuation marks.
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
    - text: The input text.

    Returns:
    None. The function will print the indented text.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimiter in ['.', '?', ':']:
        text = text.replace(delimiter, delimiter + '\n\n')

    text = '\n'.join([line.strip() for line in text.split('\n')]):
        print(text)

if __name__ == "__main__":
    text_indentation("Hello, World! How are you? I hope all is well.")
