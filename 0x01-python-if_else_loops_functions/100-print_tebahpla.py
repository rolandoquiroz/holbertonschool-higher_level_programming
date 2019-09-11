#!/usr/bin/python3
for char in range(ord('z'), ord('a') - 1, -1):
    i = 0
    if char % 2 == 1:
        i = -32
    print("{}".format(chr(char + i)), end='')
