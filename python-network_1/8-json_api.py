#!/usr/bin/python3
"""Sends a POST request to search user API with a letter parameter"""
import requests
import sys


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    try:
        r = requests.post("http://0.0.0.0:5000/search_user", data={'q': letter})
        json_res = r.json()
        if not json_res:
            print("No result")
        else:
            print("[{}] {}".format(json_res.get('id'), json_res.get('name')))
    except ValueError:
        print("Not a valid JSON")
