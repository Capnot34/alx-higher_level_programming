#!/usr/bin/python3
"""Defines a text writing function."""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8)."""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
