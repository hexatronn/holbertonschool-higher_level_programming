#!/usr/bin/python3
def no_c(my_string):
    """Return a new string without characters 'c' and 'C'"""
    new_str = ""
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            new_str += ch
    return new_str
