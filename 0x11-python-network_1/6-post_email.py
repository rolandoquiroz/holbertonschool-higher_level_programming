#!/usr/bin/python3
"""
Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""

if __name__ == "__main__":
        """ this won't be run when imported """
        from sys import argv
        from requests import post
        req = post(argv[1], data={'email': argv[2]})
        print(req.text)
