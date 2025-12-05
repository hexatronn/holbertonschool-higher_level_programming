#!/usr/bin/python3
"""Module that checks if an object inherits from a given class."""


def inherits_from(obj, a_class):
    """Return True if obj is instance of subclass of a_class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
