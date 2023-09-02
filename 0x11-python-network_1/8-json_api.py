#!/usr/bin/python3
"""
......................
"""
import sys
import requests


if __name__ == "__main__":
    l = "" if len(sys.argv) == 1 else sys.argv[1]
    pay = {"q": l}

    r = requests.post("http://0.0.0.0:5000/search_user", data=pay)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
