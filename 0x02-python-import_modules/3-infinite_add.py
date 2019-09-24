#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    s = 0
    for i in argv[1:]:
        s = s + int(i)
    print("{:d}".format(s))
