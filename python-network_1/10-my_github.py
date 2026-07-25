#!/usr/bin/python3
"""Uses GitHub API to display user id with Basic Authentication"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    r = requests.get("https://api.github.com/user", auth=(username, password))
    print(r.json().get('id'))
