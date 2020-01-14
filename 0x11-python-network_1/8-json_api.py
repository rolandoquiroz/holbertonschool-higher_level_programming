#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""

if __name__ == "__main__":
        """ this won't be run when imported """
        from sys import argv
        from requests import post
        if len(argv) == 2:
                data = {'q': argv[1]}
        else:
                data = {'q': ''}
                req = post('http://0:5000/search_user', data)
        try:
                response = req.json()
                if response.status_code == 204:
                        print('No result')
                else:
                        print("[{}] {}".format(response.get('id'),
                                               response.get('name')))
        except ValueError:
                print('Not a valid JSON')
