#!/usr/bin/python3
for i in range(25, -1, -1):
    print("{:c}{:c}".format(ord('a')+i, ord('A')+i), end='')
