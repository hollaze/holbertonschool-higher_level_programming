#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status """
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request(url='https://intranet.hbtn.io/status')

    with urllib.request.urlopen(request) as response:
        content = response.read()

    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", content.decode('utf-8'))
