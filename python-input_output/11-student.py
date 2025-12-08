#!/usr/bin/python3
"""Module that defines a Student class with JSON support."""


class Student:
    """Student class with basic attributes."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of a Student instance."""
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {
                key: getattr(self, key)
                for key in attrs
                if hasattr(self, key)
            }
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance from a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
