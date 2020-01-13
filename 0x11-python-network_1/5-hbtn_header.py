#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in
the header of the response.
"""

if __name__ == "__main__":
        """ this won't be run when imported """
        from sys import argv
        import requests
        response = requests.get(argv[1])
        print(response.headers.get('X-Request-Id'))
