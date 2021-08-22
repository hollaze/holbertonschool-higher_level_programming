#!/usr/bin/python3
""" takes URL, sends request to URL, displays value of X-Request-Id
variable found in header of response """
import urllib.request
import sys


if __name__ == "__main__":
    request = urllib.request.Request(url=sys.argv[1])

    with urllib.request.urlopen(request) as response:
        print(response.headers['X-Request-Id'])
