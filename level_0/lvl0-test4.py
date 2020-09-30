#!/usr/bin/python3
"""Cheating Voting Contest"""
import requests

url = 'http://158.69.76.135/level0.php'
myobj = {"id": '1928', "holdthedoor": "submit"}

if __name__ == "__main__":
    for i in range(0, 1024):
        requests.post(url, data=myobj)
