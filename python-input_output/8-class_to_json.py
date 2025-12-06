#!/usr/bin/python3
"""Module for JSON-serializable object dictionary."""


def class_to_json(obj):
    """Return a dictionary description of an object."""
    return obj.__dict__
