#!/usr/bin/python3
for i in range(0, 100):
    print("{:02d}{}".format(i, ", " if i <= 98 else "\n"), end='')
