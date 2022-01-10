#!/usr/bin/env python3

def zero(text):
    print("00")
    return text[::-1]

def one(text):
    print("01")
    return text[::2]

def two(t1, t2):
    print("02")
    output = ""
    for x in zip(t1, t2):
        output+= x[0] + x[1]
    return output