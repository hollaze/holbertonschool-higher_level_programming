#!/usr/bin/python3
import sys
length = len(sys.argv) -1

if length == 1:
    print("{:d} argument:".format(length))
elif length > 1:
    print("{:d} arguments:".format(length))

for i in range(0, length, 1):
    print("{:d}:".format(i + 1), sys.argv[i + 1])

if length == 0:
    print("0 arguments.")
