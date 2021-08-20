#!/usr/bin/python3
""" display value of X-Request-Id """
import urllib.request
import sys

if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])

    with urllib.request.urlopen(request) as response:
        print(response.headers['X-Request-Id'])
