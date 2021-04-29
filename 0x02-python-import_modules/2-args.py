#!/usr/bin/python3
import sys
length = len(sys.argv) - 1

if length == 1:
    print("{:d} argument:".format(length))
else:
    print("{:d}".format(length), "arguments:" if length != 0 else "arguments.")

for i in range(0, length, 1):
    print("{:d}:".format(i + 1), sys.argv[i + 1])
