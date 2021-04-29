#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv) - 1

    if length == 1:
        print("{:d} argument:".format(length))
    else:
        print("{:d}".format(length), "arguments:" if length != 0 else "arguments.")

    for i in range(0, length, 1):
        print("{:d}:".format(i + 1), argv[i + 1])
