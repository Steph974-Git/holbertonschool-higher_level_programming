#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    result = 0
    for i in range(len(roman_string)):
        if roman_string[i] not in roman_values:
            return 0
        current = roman_values[roman_string[i]]
        if i + 1 < len(roman_string) and \
           roman_values[roman_string[i + 1]] > current:
            result -= current
        else:
            result += current
    return result
