#!/usr/bin/python3
"""post an email"""
from requests import post
from sys import argv

if __name__ == "__main__":
    value = {"email": argv[2]}
    print(post(argv[1], data=value).text)
