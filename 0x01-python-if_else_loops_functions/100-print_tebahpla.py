#!/usr/bin/python3
for i in range(25, -1, -1):
    print("{:c}".format(ord('a')+i if i%2 == 0 else ord('A')+i), end='')
