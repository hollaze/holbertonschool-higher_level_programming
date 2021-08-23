#!/usr/bin/python3
"""Prints last 10 commits of a user repository"""
from requests import get
from sys import argv


if __name__ == "__main__":
    commits = get(
        "https://api.github.com/repos/{}/{}/commits?".format(
            argv[2], argv[1])).json()

    for commit in commits[:10]:
        print("{}: {}".format(commit.get("sha"), commit.get(
            "commit").get("author").get("name")))
