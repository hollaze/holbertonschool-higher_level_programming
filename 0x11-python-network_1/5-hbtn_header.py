#!/usr/bin/python3
""" takes URL, sends request to URL, displays value of X-Request-Id
variable found in header of response """
import requests
from sys import argv

if __name__ == "__main__":
    print(requests.get(argv[1]).headers["X-Request-Id"])
