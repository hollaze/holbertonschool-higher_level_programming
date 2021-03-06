#!/usr/bin/python3
"""search api"""
from requests import post
from sys import argv

if __name__ == "__main__":

    if len(argv) <= 1:
        value = ""
    else:
        value = argv[1]

    datas = {'q': value}
    response = post("http://0.0.0.0:5000/search_user", data=datas)

    try:
        json = response.json()
        if json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
