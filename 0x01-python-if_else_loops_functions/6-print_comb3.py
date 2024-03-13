#!/usr/bin/python3
for x in range(10):
    for y in range(x, 10):
        if (x != y):
            print("{}{}".format(x, y), end="")
            if (x != 8):
                print(", ", end="")
            else:
                print("")