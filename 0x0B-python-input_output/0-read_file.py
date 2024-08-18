#!/usr/bin/python3
my_file_0 = __import__("my_file_0.txt")
def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        text = f.read()
        print(text, end="")
