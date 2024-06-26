#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    temp = 0
    for i in reversed(roman_string):
        temp = dic[i]
        total += temp if total < temp * 5 else - temp
    return total
