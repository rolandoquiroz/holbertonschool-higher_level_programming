#!/usr/bin/python3
"""
Describe me
"""

if __name__ == "__main__":
        """ this won't be run when imported """
        from urllib import request
        with request.urlopen("https://intranet.hbtn.io/status") as response:
                data = response.read()
                print("Body response:")
                print("\t- type: {}".format(type(data)))
                print("\t- content: {}".format(data))
                print("\t- utf8 content: {}".format(data.decode('utf8')))
