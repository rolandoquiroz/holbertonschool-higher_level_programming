#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""

if __name__ == "__main__":
        """ this won't be run when imported """
        from sys import argv
        from requests import get
        req = get(argv[1])
        if (req.status_code < 400):
                print(req.text)
        else:
                print('Error code:', req.status_code)
