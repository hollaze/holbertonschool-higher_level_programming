#!/usr/bin/python3
""" takes URL and email, sends POST request to URL with email
as parameter, displays body decoded in utf-8 """
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("utf-8")

    request = urllib.request.Request(url, data)

    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
