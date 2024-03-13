#!/usr/bin/python3
for n in range(121, 96, -2):
    print("{:c}{:c}".format(n + 1, n - 32), end="")
