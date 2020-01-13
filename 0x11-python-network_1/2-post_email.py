#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

if __name__ == "__main__":
        """ this won't be run when imported """
        from sys import argv
        from urllib import request, parse
        values = {'email': argv[2]}
        data = parse.urlencode(values)
        data = data.encode('utf-8')
        req = request.Request(argv[1], data)
        with request.urlopen(req) as response:
                response_data = response.read()
                print(response_data.decode('utf-8'))
