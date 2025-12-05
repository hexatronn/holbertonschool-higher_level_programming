#!/usr/bin/python3
"""Module that checks object instance or subclass relationship."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or its subclass."""
    return isinstance(obj, a_class)
