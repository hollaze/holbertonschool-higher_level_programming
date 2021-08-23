#!/usr/bin/python3
"""using github api"""
from requests import get
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/user"

    response = get(url, auth=(argv[1], argv[2]))
    json = response.json()
    print(json.get('id'))
