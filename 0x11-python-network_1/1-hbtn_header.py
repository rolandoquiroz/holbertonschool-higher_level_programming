#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in
the header of the response.
"""

if __name__ == "__main__":
        """ this won't be run when imported """
        from sys import argv
        from urllib import request
        with request.urlopen(argv[1]) as response:
                print(response.getheader('X-Request-Id'))
