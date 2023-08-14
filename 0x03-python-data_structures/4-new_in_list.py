#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    # Generate a new list using a list comprehension and conditionals
    new_list = [element if i == idx else val for i, val in enumerate(my_list)]
    
    return new_list
