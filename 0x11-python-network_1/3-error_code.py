#!/usr/bin/python3
"""takes URL, sends request to URL, displays body"""
import urllib.request
import urllib.error
from sys import argv

if __name__ == "__main__":
    try:
        url = argv[1]
        request = urllib.request.Request(url)

        with urllib.request.urlopen(url) as response:
            print(response.read().decode("utf-8"))

    except urllib.error.HTTPError as http_error:
        print("Error code:", http_error.code)
