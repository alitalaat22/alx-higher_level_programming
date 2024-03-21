#!/usr/bin/python3
def multiple_returns(sentence):
    lenth = len(sentence)
    if lenth == 0:
        return 0, None
    else:
        f = sentence[0]
        return lenth, f
