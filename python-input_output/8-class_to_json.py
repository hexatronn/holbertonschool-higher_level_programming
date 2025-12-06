#!/usr/bin/python3
"""Module that returns a dictionary description of an object for JSON serialization."""


def class_to_json(obj):
    """Return the dictionary representation of a simple data structure object."""
    return obj.__dict__
