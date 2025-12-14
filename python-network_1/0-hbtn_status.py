#!/usr/bin/python3
"""
Fetches the URL https://intranet.hbtn.io/status using urllib
and displays information about the response body.
"""

import urllib.request


def main():
    """Send a GET request and print the response body details."""
    url = "https://intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        body = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode("utf-8")))


if __name__ == "__main__":
    main()
