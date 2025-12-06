#!/usr/bin/python3
"""Module that writes and prints a text file."""


def write_file(filename="", text=""):
    """Writes a UTF-8 text file and prints it to stdout."""
    with open(filename, "w", encoding="utf-8") as f:
        print(f.write(), end="")
