#!/usr/bin/python3
"""Error code"""
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    status = response.status_code

    if status >= 400:
        print("Error code:", status)
    else:
        print(response.text)
