#!/usr/bin/python3
"""search api"""
from requests import post
from sys import argv

if __name__ == "__main__":

    if len(argv) <= 1:
        value = ''
    else:
        value = argv[1]

    datas = {'q': value}
    json_response = post(
        " http://ac5942ef3eb7.c0cd6e92.hbtn-cod.io:5000/search_user",
        data=datas).json()

    try:
        if 'id' in json:
            print("[{}] {}".format(json_response["id"], json_response["name"]))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
