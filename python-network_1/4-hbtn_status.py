#!/usr/bin/python3
"""Fetches a URL and displays the response body."""

import requests


if __name__ == "__main__":
    response = requests.get("https://intranet.hbtn.io/status")
    content = response.text

    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
