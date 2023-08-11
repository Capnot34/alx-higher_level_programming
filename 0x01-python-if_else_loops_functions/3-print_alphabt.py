#!/usr/bin/python3
for letters in range(97, 123):
    if letters != ord('q') and letters != ord('e'):
        print("{:c}".format(letters), end="")
