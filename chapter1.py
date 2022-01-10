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

def three(text):
    print("03")
    parts = text.split(" ")

    # Only count letters
    lst = [len((''.join(filter(str.isalpha, x)))) for x in parts]
    return lst

def four(text):
    print("04")
    parts = text.split(" ")
    set1, set2 = [], []

    set1+= [''.join(parts[0])]
    set2+= parts[1:5]

    set1+= parts[5:10]
    set2+= parts[10:15]

    set1+= parts[15:17]
    set2+= parts[17:19]

    set1+= [''.join(parts[19])]
    set2+= parts[20:]

    result1 = [x[0] for x in set1]
    result2 = [x[0:2] for x in set2]

    j = len(parts)

    s = list(range(j))
    s1 = [s[0]] + s[5:10] + s[15:17] + [s[19]]
    s2 = s[1:5] + s[10:15] + s[17:19] + s[20:]

    result = []
    result+= list(zip(result1, s1))
    result+= list(zip(result2, s2))

    output = {}

    output = dict(result)
    return output