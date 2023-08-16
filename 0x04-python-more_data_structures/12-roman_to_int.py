#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    num = 0
    prev_value = 0
    for symbol in reversed(roman_string):
        if roman_dict[symbol] < prev_value:
            num -= roman_dict[symbol]
        else:
            num += roman_dict[symbol]
        prev_value = roman_dict[symbol]

    return num
