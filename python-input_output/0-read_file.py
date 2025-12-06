#!/usr/bin/python3
"""Module that reads and prints a text file.""" 
def read_file(filename=""):
        """Reads a UTF-8 text file and prints it to stdout."""
	with open('my_file_0.txt', 'r', encoding="utf-8") as f:
	print(f.read())

