#!/usr/bin/python3
[print("{:02d}{}".format(i, ", " if i <= 98 else "\n"), end='') for i in range(0, 100)]
