#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    total_number = 0

    number = 0

    digits = {'I': 1, 'V':5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for i in reversed(roman_string):
        number = digits[i]
        total_number = number if total_number < number * 5 else -number
    return total_number
