#!/usr/bin/python3
import sys
if __name__ == "__main__":
    s = 0
    for i in range(1, len(sys.argv)):
        s = s + int(sys.argv[i])
        print("{}".format(s))
