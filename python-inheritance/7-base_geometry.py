#!/usr/bin/python3
"""
Module that defines the BaseGeometry class with integer validation.
"""


class BaseGeometry:
    """
    Base class for geometry.
    """

    def area(self):
        """
        Raises an Exception with the message:
        area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is an integer > 0.

        Args:
            name (str): The name of the parameter
            value (int): The value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value <= 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
