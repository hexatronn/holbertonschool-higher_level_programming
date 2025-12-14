#!/usr/bin/python3
"""
Sends a request to a given URL and displays the value of
the X-Request-Id header from the response.
"""

import sys
import urllib.request


def main():
    """Fetch the URL and print the X-Request-Id header value."""
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        headers = response.headers
        print(headers.get("X-Request-Id"))


if __name__ == "__main__":
    main()
